#from flask import Flask, render_template, request,json, jsonify,Response,make_response,redirect
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from sqlalchemy.sql.functions import current_timestamp
from models import *

app = Flask(__name__)
#app.debug = True

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///../app/circular.db'
#app.config['SQLALCHEMY_ECHO'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

#--- member 全件読み取り　-----
members = Member.query.all()
for member in members:
    print(member)

#--- circular 全件読み取り　-----

circulars = Circular.query.all()
for circular in circulars:
    print(circular.to_dict())
    for item in circular.items:
        print(item.to_dict())
