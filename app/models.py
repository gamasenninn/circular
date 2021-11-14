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
    phone_number = db.Column(db.String(20))
    memo = db.Column(db.UnicodeText)
    email = db.Column(db.String(120))
    updated_at = db.Column(db.DateTime(timezone=True), nullable=False, server_default=current_timestamp())
    created_at = db.Column(db.DateTime(timezone=True), nullable=False, server_default=current_timestamp())

    def __repr__(self):
        return f'<Member {self.id},{self.name}>'

    def to_dict(self):
        return {
            "member_name": self.name,
            "phone_number": self.phone_number,
            "memo" : self.memo,
            "email": self.email,
            "updated_at": self.updated_at, 
            "created_at": self.created_at, 
        }

class Circular(db.Model):
    __tablename__ = 'circulars'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.UnicodeText)
    detail = db.Column(db.UnicodeText)
    due_date = db.Column(db.Date)
    updated_at = db.Column(db.DateTime(timezone=True), nullable=False, server_default=current_timestamp())
    created_at = db.Column(db.DateTime(timezone=True), nullable=False, server_default=current_timestamp())
    items = db.relationship('CircularItem',backref="circulars")

    def __repr__(self):
        return f'<Circular {self.id},{self.title}>'

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "detail" : self.detail,
            "due_date": self.due_date,
            "updated_at": self.updated_at, 
            "created_at": self.created_at, 
        }

class CircularItem(db.Model):
    __tablename__ = 'circular_items'
    id = db.Column(db.Integer, primary_key=True)
    member_id = db.Column(db.Integer)
    person = db.Column(db.Text)
    department_id = db.Column(db.Integer)
    confirm = db.Column(db.String(50))
    memo = db.Column(db.Text)
    update_at = db.Column(db.DateTime(timezone=True), nullable=False, server_default=current_timestamp())
    created_at = db.Column(db.DateTime(timezone=True), nullable=False, server_default=current_timestamp())
    #circular_id = db.Column(db.Integer)
    circular_id = db.Column(db.Integer,db.ForeignKey('circulars.id'))

    def __repr__(self):
        return f'<CircularItem {self.id},{self.person}>'

    def to_dict(self):
        return {
            "id": self.id,
            "circular_id": self.circular_id,
            "member_id": self.member_id,
            "person" : self.person,
            "department_id": self.department_id,
            "confirm": self.confirm,
            "memo": self.memo,
        }
