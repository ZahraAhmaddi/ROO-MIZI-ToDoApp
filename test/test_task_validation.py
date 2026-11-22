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


if __name__ == "__main__":
    unittest.main()
