import unittest
from pathlib import Path

from flask import Flask

from app import db
from app.models import Task
from app.routes import init_routes


class TaskValidationTests(unittest.TestCase):
    def setUp(self):
        template_folder = Path(__file__).resolve().parents[1] / "app" / "templates"
        self.app = Flask(__name__, template_folder=str(template_folder))
        self.app.config.update(
            SECRET_KEY="test",
            SQLALCHEMY_DATABASE_URI="sqlite://",
            SQLALCHEMY_TRACK_MODIFICATIONS=False,
        )
        db.init_app(self.app)
        init_routes(self.app)

        with self.app.app_context():
            db.create_all()

        self.client = self.app.test_client()

    def tearDown(self):
        with self.app.app_context():
            db.session.remove()
            db.drop_all()

    def test_add_accepts_unicode_and_multiline_description(self):
        response = self.client.post(
            "/add-task",
            data={
                "title": "  Reunión — café ☕  ",
                "description": "First line\nSecond line\twith tab",
            },
            follow_redirects=True,
        )

        self.assertIn(b"Task created successfully.", response.data)
        with self.app.app_context():
            task = Task.query.one()
            self.assertEqual(task.title, "Reunión — café ☕")
            self.assertEqual(task.description, "First line\nSecond line\twith tab")

    def test_add_rejects_empty_and_invisible_titles(self):
        invalid_titles = (
            ("   ", "Task title cannot be empty."),
            (
                "\u200b\u200d",
                "Task title must include at least one visible character.",
            ),
            (
                "two\nlines",
                "Task title cannot contain line breaks or control characters.",
            ),
        )

        for title, expected_error in invalid_titles:
            with self.subTest(title=repr(title)):
                response = self.client.post(
                    "/add-task",
                    data={"title": title, "description": ""},
                    follow_redirects=True,
                )
                self.assertIn(expected_error.encode(), response.data)

        with self.app.app_context():
            self.assertEqual(Task.query.count(), 0)

    def test_add_rejects_overlong_fields_and_control_characters(self):
        long_title_response = self.client.post(
            "/add-task",
            data={"title": "t" * 101, "description": ""},
            follow_redirects=True,
        )
        self.assertIn(
            b"Task title cannot exceed 100 characters.",
            long_title_response.data,
        )

        response = self.client.post(
            "/add-task",
            data={
                "title": "valid\x00title",
                "description": "x" * 2001 + "\x00",
            },
            follow_redirects=True,
        )

        self.assertIn(
            b"Task title cannot contain line breaks or control characters.",
            response.data,
        )
        self.assertIn(b"Description cannot exceed 2,000 characters.", response.data)
        self.assertIn(
            b"Description contains unsupported control characters.",
            response.data,
        )
        with self.app.app_context():
            self.assertEqual(Task.query.count(), 0)

    def test_add_rejects_invisible_description(self):
        response = self.client.post(
            "/add-task",
            data={"title": "Visible title", "description": "\u200b\u200d"},
            follow_redirects=True,
        )

        self.assertIn(
            b"Description must include at least one visible character.",
            response.data,
        )
        with self.app.app_context():
            self.assertEqual(Task.query.count(), 0)

    def test_edit_uses_validation_without_changing_existing_task(self):
        with self.app.app_context():
            task = Task(title="Original", description="Keep this")
            db.session.add(task)
            db.session.commit()
            task_id = task.id

        response = self.client.post(
            f"/edit-task/{task_id}",
            data={"title": "Changed", "description": "invalid\x01text"},
            follow_redirects=True,
        )

        self.assertIn(b"Description contains unsupported control characters.", response.data)
        with self.app.app_context():
            task = db.session.get(Task, task_id)
            self.assertEqual(task.title, "Original")
            self.assertEqual(task.description, "Keep this")

    def test_length_limits_accept_their_boundaries(self):
        response = self.client.post(
            "/add-task",
            data={"title": "t" * 100, "description": "d" * 2000},
            follow_redirects=True,
        )

        self.assertIn(b"Task created successfully.", response.data)
        with self.app.app_context():
            task = Task.query.one()
            self.assertEqual(len(task.title), 100)
            self.assertEqual(len(task.description), 2000)


    def test_add_task_uses_todo_as_default_status(self):
        response = self.client.post(
            "/add-task",
            data={"title": "Default status", "description": ""},
            follow_redirects=True,
        )

        self.assertIn(b"Task created successfully.", response.data)
        with self.app.app_context():
            task = Task.query.one()
            self.assertEqual(task.status, "TODO")
            self.assertIsNone(task.description)

    def test_add_task_redirects_to_home(self):
        response = self.client.post(
            "/add-task",
            data={"title": "Redirect check", "description": ""},
        )

        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.headers["Location"], "/")

    def test_home_page_renders_empty_board(self):
        response = self.client.get("/")

        self.assertEqual(response.status_code, 200)
        self.assertIn(b"To Do", response.data)
        self.assertIn(b"In Progress", response.data)
        self.assertIn(b"Completed", response.data)
        self.assertIn(b"No tasks yet. Add one to get started!", response.data)

    def test_home_page_displays_tasks_in_their_status_columns(self):
        with self.app.app_context():
            db.session.add_all([
                Task(title="Visible todo", status="TODO"),
                Task(title="Visible progress", status="IN_PROGRESS"),
                Task(title="Visible completed", status="DONE"),
            ])
            db.session.commit()

        response = self.client.get("/")

        self.assertEqual(response.status_code, 200)
        for title in (b"Visible todo", b"Visible progress", b"Visible completed"):
            with self.subTest(title=title):
                self.assertIn(title, response.data)

    def test_edit_task_updates_title_and_description(self):
        with self.app.app_context():
            task = Task(title="Before edit", description="Old description")
            db.session.add(task)
            db.session.commit()
            task_id = task.id

        response = self.client.post(
            f"/edit-task/{task_id}",
            data={"title": "After edit", "description": "Updated description"},
            follow_redirects=True,
        )

        self.assertIn(b"Task updated successfully.", response.data)
        with self.app.app_context():
            task = db.session.get(Task, task_id)
            self.assertEqual(task.title, "After edit")
            self.assertEqual(task.description, "Updated description")

    def test_edit_task_can_clear_description(self):
        with self.app.app_context():
            task = Task(title="Keep title", description="Remove this")
            db.session.add(task)
            db.session.commit()
            task_id = task.id

        response = self.client.post(
            f"/edit-task/{task_id}",
            data={"title": "Keep title", "description": "   "},
            follow_redirects=True,
        )

        self.assertIn(b"Task updated successfully.", response.data)
        with self.app.app_context():
            task = db.session.get(Task, task_id)
            self.assertIsNone(task.description)

    def test_edit_task_returns_not_found_for_unknown_id(self):
        response = self.client.post(
            "/edit-task/9999",
            data={"title": "Does not matter", "description": ""},
            follow_redirects=True,
        )

        self.assertIn(b"Task not found. It may have been deleted.", response.data)
        with self.app.app_context():
            self.assertEqual(Task.query.count(), 0)

    def test_update_status_accepts_each_supported_status(self):
        for status in ("IN_PROGRESS", "DONE", "TODO"):
            with self.subTest(status=status):
                with self.app.app_context():
                    task = Task(title=f"Status {status}")
                    db.session.add(task)
                    db.session.commit()
                    task_id = task.id

                response = self.client.post(
                    f"/update-status/{task_id}",
                    data={"status": status.lower()},
                    follow_redirects=True,
                )

                self.assertIn(b"Task status updated successfully.", response.data)
                with self.app.app_context():
                    task = db.session.get(Task, task_id)
                    self.assertEqual(task.status, status)
                    db.session.delete(task)
                    db.session.commit()

    def test_update_status_rejects_unsupported_value(self):
        with self.app.app_context():
            task = Task(title="Status stays the same")
            db.session.add(task)
            db.session.commit()
            task_id = task.id

        response = self.client.post(
            f"/update-status/{task_id}",
            data={"status": "ARCHIVED"},
            follow_redirects=True,
        )

        self.assertIn(b"Invalid task status.", response.data)
        with self.app.app_context():
            task = db.session.get(Task, task_id)
            self.assertEqual(task.status, "TODO")

    def test_update_status_returns_not_found_for_unknown_id(self):
        response = self.client.post(
            "/update-status/9999",
            data={"status": "DONE"},
            follow_redirects=True,
        )

        self.assertIn(b"Task not found.", response.data)

    def test_delete_task_removes_existing_task(self):
        with self.app.app_context():
            task = Task(title="Delete me", description="Temporary")
            db.session.add(task)
            db.session.commit()
            task_id = task.id

        response = self.client.post(
            f"/delete-task/{task_id}",
            follow_redirects=True,
        )

        self.assertIn(b"Task deleted successfully.", response.data)
        with self.app.app_context():
            self.assertIsNone(db.session.get(Task, task_id))
            self.assertEqual(Task.query.count(), 0)

    def test_delete_task_returns_not_found_for_unknown_id(self):
        response = self.client.post(
            "/delete-task/9999",
            follow_redirects=True,
        )

        self.assertIn(
            b"Task not found. It may have already been deleted.",
            response.data,
        )
        with self.app.app_context():
            self.assertEqual(Task.query.count(), 0)

    def test_tasks_are_displayed_newest_first(self):
        with self.app.app_context():
            from datetime import datetime, timedelta

            older = Task(
                title="Older task",
                created_at=datetime(2026, 1, 1, 10, 0, 0),
            )
            newer = Task(
                title="Newer task",
                created_at=datetime(2026, 1, 2, 10, 0, 0),
            )
            db.session.add_all([older, newer])
            db.session.commit()

        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertLess(
            response.data.index(b"Newer task"),
            response.data.index(b"Older task"),
        )



if __name__ == "__main__":
    unittest.main()
