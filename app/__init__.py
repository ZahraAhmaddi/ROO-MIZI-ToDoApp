from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from urllib.parse import quote_plus

db = SQLAlchemy()


def create_app():
    app = Flask(__name__)

    connection_string = (
        "DRIVER={ODBC Driver 18 for SQL Server};"
        "SERVER=localhost;"
        "DATABASE=TodoApp;"
        "Trusted_Connection=yes;"
        "TrustServerCertificate=yes;"
    )

    params = quote_plus(connection_string)

    app.config["SQLALCHEMY_DATABASE_URI"] = (
        "mssql+pyodbc:///?odbc_connect=" + params
    )

    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.init_app(app)
    from app.models import Task

    with app.app_context():
         db.create_all()
    from app.routes import init_routes
    init_routes(app)
    return app