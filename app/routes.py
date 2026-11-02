from flask import render_template
from app import db
from app.models import Task
def init_routes(app):
    @app.route("/")
    def index():
        tasks=Task.query.order_by(Task.created_at.desc()).all()
        return render_template(
            "index.html",
            tasks=tasks
        )
    