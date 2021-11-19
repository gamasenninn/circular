"""flask appの初期化を行い、flask appオブジェクトの実体を持つ"""
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from flask_sample.database import init_db
import flask_sample.models


def create_app():
    app = Flask(__name__)
    app.config.from_object('flask_sample.config.Config')

    init_db(app)

    return app

app = create_app()


users = User.query.all()