from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from models import db,Member,Circular,CircularItem
from sqlalchemy_seed import create_table,drop_table,load_fixtures,load_fixture_files

app = Flask(__name__)

app.debug = True

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///circular.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
#app.config['SQLALCHEMY_ECHO'] = True
db = SQLAlchemy(app)

models = [Member,Circular,CircularItem]

for model in models:
    db.session.query(model).delete()
    db.session.commit()

fixtures = load_fixture_files('./seeds',
    [
        'members.yaml',
        'circulars.yaml',
        'circularItems.yaml',
    ])
load_fixtures(db.session,fixtures)