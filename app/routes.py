
from flask import render_template, request, redirect, url_for, flash
from app import db
from app.models import Task


def init_routes(app):

    @app.route("/", methods=["GET"])
    def index():
        tasks = Task.query.order_by(
            Task.created_at.desc()
        ).all()

        todo_tasks = [
            task for task in tasks
            if task.status == "TODO"
        ]

        progress_tasks = [
            task for task in tasks
            if task.status == "IN_PROGRESS"
        ]

        done_tasks = [
            task for task in tasks
            if task.status == "DONE"
        ]

        return render_template(
            "index.html",
            todo_tasks=todo_tasks,
            progress_tasks=progress_tasks,
            done_tasks=done_tasks
        )

    @app.route("/add-task", methods=["POST"])
    def add_task():

        title = request.form.get("title", "").strip()

        description = request.form.get(
            "description", ""
        ).strip()

        # Validate title and description
        if not title:
            flash("Task title cannot be empty.", "error")
            return redirect(url_for("index"))

        if len(title) > 100:
            flash("Task title cannot exceed 100 characters.", "error")
            return redirect(url_for("index"))

        if len(description) > 2000:
            flash("Description cannot exceed 2,000 characters.", "error")
            return redirect(url_for("index"))

        new_task = Task(
            title=title,
            description=description if description else None,
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
        task = Task.query.get_or_404(task_id)
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

            flash("Failed to update task status. Please try again.", "error")

        return redirect(url_for("index"))
