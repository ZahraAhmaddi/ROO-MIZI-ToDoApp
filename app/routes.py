
import unicodedata

from flask import render_template, request, redirect, url_for, flash
from app import db
from app.models import Task

MAX_TITLE_LENGTH = 100
MAX_DESCRIPTION_LENGTH = 2000


def _has_invalid_control_characters(value, allow_multiline=False):
    allowed_controls = "\r\n\t" if allow_multiline else ""
    return any(
        unicodedata.category(character) in {"Cc", "Cs"}
        and character not in allowed_controls
        for character in value
    )


def _has_visible_characters(value):
    return any(
        not character.isspace()
        and not unicodedata.category(character).startswith("C")
        for character in value
    )


def validate_task_fields(title, description):
    title = title.strip()
    description = description.strip()
    errors = []

    if not title:
        errors.append("Task title cannot be empty.")
    else:
        if len(title) > MAX_TITLE_LENGTH:
            errors.append(
                f"Task title cannot exceed {MAX_TITLE_LENGTH} characters."
            )

        invalid_title_characters = (
            _has_invalid_control_characters(title)
            or any(character in "\u2028\u2029" for character in title)
        )
        if invalid_title_characters:
            errors.append(
                "Task title cannot contain line breaks or control characters."
            )
        elif not _has_visible_characters(title):
            errors.append("Task title must include at least one visible character.")

    if len(description) > MAX_DESCRIPTION_LENGTH:
        errors.append(
            f"Description cannot exceed {MAX_DESCRIPTION_LENGTH:,} characters."
        )

    invalid_description_characters = _has_invalid_control_characters(
        description,
        allow_multiline=True
    )
    if invalid_description_characters:
        errors.append("Description contains unsupported control characters.")
    elif description and not _has_visible_characters(description):
        errors.append("Description must include at least one visible character.")

    return title, description or None, errors


def init_routes(app):

    @app.route("/", methods=["GET"])
    def index():
        tasks = Task.query.order_by(Task.created_at.desc()).all()

        todo_tasks = [task for task in tasks if task.status == "TODO"]
        progress_tasks = [task for task in tasks if task.status == "IN_PROGRESS"]
        done_tasks = [task for task in tasks if task.status == "DONE"]

        return render_template(
            "index.html",
            todo_tasks=todo_tasks,
            progress_tasks=progress_tasks,
            done_tasks=done_tasks
        )

    @app.route("/add-task", methods=["POST"])
    def add_task():
        title, description, errors = validate_task_fields(
            request.form.get("title", ""),
            request.form.get("description", "")
        )

        if errors:
            for error in errors:
                flash(error, "error")
            return redirect(url_for("index"))

        new_task = Task(
            title=title,
            description=description,
            status="TODO"
        )

        try:
            db.session.add(new_task)
            db.session.commit()
            flash("Task created successfully.", "success")
        except Exception:
            db.session.rollback()
            app.logger.exception("Error while saving task")
            flash("Failed to save task. Please try again.", "error")

        return redirect(url_for("index"))

    @app.route("/update-status/<int:task_id>", methods=["POST"])
    def update_status(task_id):
        task = db.session.get(Task, task_id)

        if task is None:
            flash("Task not found.", "error")
            return redirect(url_for("index"))

        new_status = request.form.get("status", "").upper()
        allowed_statuses = {"TODO", "IN_PROGRESS", "DONE"}

        if new_status not in allowed_statuses:
            flash("Invalid task status.", "error")
            return redirect(url_for("index"))

        try:
            task.status = new_status
            db.session.commit()
            flash("Task status updated successfully.", "success")
        except Exception:
            db.session.rollback()
            app.logger.exception("Error while updating task status")
            flash("Failed to update task status.", "error")

        return redirect(url_for("index"))

    @app.route("/edit-task/<int:task_id>", methods=["POST"])
    def edit_task(task_id):
        task = db.session.get(Task, task_id)

        if task is None:
            flash("Task not found. It may have been deleted.", "error")
            return redirect(url_for("index"))

        title, description, errors = validate_task_fields(
            request.form.get("title", ""),
            request.form.get("description", "")
        )

        if errors:
            for error in errors:
                flash(error, "error")
            return redirect(url_for("index"))

        try:
            task.title = title
            task.description = description
            db.session.commit()
            flash("Task updated successfully.", "success")
        except Exception:
            db.session.rollback()
            app.logger.exception("Error while editing task")
            flash("Failed to update task.", "error")

        return redirect(url_for("index"))

    @app.route("/delete-task/<int:task_id>", methods=["POST"])
    def delete_task(task_id):
        task = db.session.get(Task, task_id)

        if task is None:
            flash("Task not found. It may have already been deleted.", "error")
            return redirect(url_for("index"))

        try:
            db.session.delete(task)
            db.session.commit()
            flash("Task deleted successfully.", "success")
        except Exception:
            db.session.rollback()
            app.logger.exception("Error while deleting task")
            flash("Failed to delete task.", "error")

        return redirect(url_for("index"))


