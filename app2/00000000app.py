"""flask appの初期化を行い、flask appオブジェクトの実体を持つ"""
from flask import Flask

from database import init_db

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')

    init_db(app)

    return app

app = create_app()

