from datetime import datetime
from database import db


class Member(db.Model):
    __tablename__ = 'members'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120))
    category = db.Column(db.String(50))
    telNumber = db.Column(db.String(20))
    memo = db.Column(db.Text)
    email = db.Column(db.String(120))

    def __repr__(self):
        return f'<Member {self.id},{self.name}>'

    def to_dict(self):
        return {
            "name": self.name,
            "telNumber": self.telNumber,
            "memo" : self.memo,
            "email": self.email,
        }

class Circular(db.Model):
    __tablename__ = 'circulars'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.Text)
    detail = db.Column(db.Text)
    dueDate = db.Column(db.Date)
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



