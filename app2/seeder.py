from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from models import Member,Circular,CircularItem

app = Flask(__name__)
app.config.from_object('config.Config')

db = SQLAlchemy(app)

Member.query.all()

#members = Member.query.all()



'''
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from database import init_db
import models as m

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')

    init_db(app)

    return app

app = create_app()
db = SQLAlchemy(app)

members = m.Member.query.all()
'''




'''
#from app import app

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

'''
