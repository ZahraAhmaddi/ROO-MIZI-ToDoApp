from datetime import datetime
from app import db


class Task(db.Model):
    __tablename__ = "tasks"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    title = db.Column(db.String(100), nullable=False)

    description = db.Column(db.String(2000), nullable=True)

    # Default task status is TODO
    status = db.Column(db.String(20), nullable=False, default="TODO")

    created_at = db.Column(
        db.DateTime,
        nullable=False,
        default=datetime.now
    )