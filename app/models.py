#from flask import Flask, render_template, request,json, jsonify,Response,make_response,redirect
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from sqlalchemy.sql.functions import current_timestamp

app = Flask(__name__)
#app.debug = True

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///circular.db'
app.config['SQLALCHEMY_ECHO'] = False
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

#migrate = Migrate(app,db)
migrate = Migrate(app,db,render_as_batch=True)
#Caution if you use SQLITE, adding <render_as_batch=True> . This option is batch mode .


class Member(db.Model):
    __tablename__ = 'members'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Unicode(120))
    category = db.Column(db.Unicode(50))
    telNumber = db.Column(db.String(20))
    memo = db.Column(db.UnicodeText)
    email = db.Column(db.String(120))
    updatedAt = db.Column(db.DateTime(timezone=True), nullable=False, server_default=current_timestamp())
    createdAt = db.Column(db.DateTime(timezone=True), nullable=False, server_default=current_timestamp())

    def __repr__(self):
        return f'<Member {self.id},{self.name}>'

    def to_dict(self):
        return {
            "name": self.name,
            "telNumber": self.telNumber,
            "memo" : self.memo,
            "email": self.email,
            "updatedAt": self.updatedAt, 
            "createdAt": self.createdAt, 
        }

class Circular(db.Model):
    __tablename__ = 'circulars'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.UnicodeText)
    detail = db.Column(db.UnicodeText)
    dueDate = db.Column(db.Date)
    updatedAt = db.Column(db.DateTime(timezone=True), nullable=False, server_default=current_timestamp())
    createdAt = db.Column(db.DateTime(timezone=True), nullable=False, server_default=current_timestamp())
    items = db.relationship('CircularItem',backref="circulars")

    def __repr__(self):
        return f'<Circular {self.id},{self.title}>'

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "detail" : self.detail,
            "dueDate": self.dueDate,
            "updatedAt": self.updatedAt, 
            "createdAt": self.createdAt, 
        }

class CircularItem(db.Model):
    __tablename__ = 'circularItems'
    id = db.Column(db.Integer, primary_key=True)
    memberId = db.Column(db.Integer)
    person = db.Column(db.Text)
    departmentId = db.Column(db.Integer)
    confirm = db.Column(db.String(50))
    memo = db.Column(db.Text)
    updatedAt = db.Column(db.DateTime(timezone=True), nullable=False, server_default=current_timestamp())
    createdAt = db.Column(db.DateTime(timezone=True), nullable=False, server_default=current_timestamp())
    #circular_id = db.Column(db.Integer)
    circularId = db.Column(db.Integer,db.ForeignKey('circulars.id'))

    def __repr__(self):
        return f'<CircularItem {self.id},{self.person}>'

    def to_dict(self):
        return {
            "id": self.id,
            "circularId": self.circularId,
            "memberId": self.memberId,
            "person" : self.person,
            "departmentId": self.departmentId,
            "confirm": self.confirm,
            "memo": self.memo,
        }
