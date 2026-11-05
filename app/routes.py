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
            if task.status == "todo"
        ]

        progress_tasks = [
            task for task in tasks
            if task.status == "in_progress"
        ]

        done_tasks = [
            task for task in tasks
            if task.status == "done"
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

        # Validate title
        if not title:
            flash("عنوان وظیفه نمی‌تواند خالی باشد.", "error")
            return redirect(url_for("index"))

        if len(title) > 100:
            flash("عنوان نباید بیشتر از ۱۰۰ کاراکتر باشد.", "error")
            return redirect(url_for("index"))

        if len(description) > 2000:
            flash("توضیحات نباید بیشتر از ۲۰۰۰ کاراکتر باشد.", "error")
            return redirect(url_for("index"))

        new_task = Task(
            title=title,
            description=description if description else None,
            status="TODO"
        )

        try:
            db.session.add(new_task)
            db.session.commit()

            flash("وظیفه با موفقیت ثبت شد.", "success")

        except Exception:
            db.session.rollback()
            app.logger.exception("Error while saving task")

            flash("خطا در ذخیره وظیفه رخ داد.", "error")

        return redirect(url_for("index"))
    