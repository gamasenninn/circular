"""FlaskのConfigを提供する"""
import os


class DevelopmentConfig:

    # Flask
    DEBUG = True

    # SQLAlchemy
    SQLALCHEMY_DATABASE_URI = 'sqlite:///circular.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = False

Config = DevelopmentConfig