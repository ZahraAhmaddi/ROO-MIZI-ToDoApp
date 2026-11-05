from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

db = SQLAlchemy()


def create_app():
    app = Flask(__name__)

    app.config["SECRET_KEY"] = os.environ.get(
        "SECRET_KEY",
        "dev-secret-key-change-me"
    )

    # SQLite database
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///tasks.db"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.init_app(app)

    from app.models import Task

    with app.app_context():
        db.create_all()

    from app.routes import init_routes
    init_routes(app)

    return app