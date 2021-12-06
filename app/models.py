from app import db,app,ma
#from sqlalchemy.sql.functions import current_timestamp
from datetime import datetime

class Member(db.Model):
    __tablename__ = 'members'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120))
    department = db.Column(db.String(50))
    telNumber = db.Column(db.String(20))
    memo = db.Column(db.Text)
    email = db.Column(db.String(120))
    createdAt = db.Column(db.DateTime, nullable=False, default=datetime.now)
    updatedAt = db.Column(db.DateTime, nullable=False,
                          default=datetime.now, onupdate=datetime.now)    
#    updatedAt = db.Column(db.DateTime(timezone=True), nullable=False, server_default=current_timestamp())
#    createdAt = db.Column(db.DateTime(timezone=True), nullable=False, server_default=current_timestamp())

    def __repr__(self):
        return f'<Member {self.id},{self.name}>'


class Circular(db.Model):
    __tablename__ = 'circulars'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.Text)
    detail = db.Column(db.Text)
    dueDate = db.Column(db.Date)
    createdAt = db.Column(db.DateTime, nullable=False, default=datetime.now)
    updatedAt = db.Column(db.DateTime, nullable=False,
                          default=datetime.now, onupdate=datetime.now)    
#    updatedAt = db.Column(db.DateTime(timezone=True), nullable=False, server_default=current_timestamp())
#    createdAt = db.Column(db.DateTime(timezone=True), nullable=False, server_default=current_timestamp())
    items = db.relationship('CircularItem',backref="circulars")

    def __repr__(self):
        return f'<Circular {self.id},{self.title}>'


class CircularItem(db.Model):
    __tablename__ = 'circularItems'
    id = db.Column(db.Integer, primary_key=True)
    memberId = db.Column(db.Integer)
    person = db.Column(db.Text)
    department = db.Column(db.String(50))
    confirm = db.Column(db.String(20))
    memo = db.Column(db.Text)
    createdAt = db.Column(db.DateTime, nullable=False, default=datetime.now)
    updatedAt = db.Column(db.DateTime, nullable=False,
                          default=datetime.now, onupdate=datetime.now)    
    #updatedAt = db.Column(db.DateTime(timezone=True), nullable=False, server_default=current_timestamp())
    #createdAt = db.Column(db.DateTime(timezone=True), nullable=False, server_default=current_timestamp())
    #circular_id = db.Column(db.Integer)
    circularId = db.Column(db.Integer,db.ForeignKey('circulars.id'))

    def __repr__(self):
        return f'<CircularItem {self.id},{self.person}>'


class MemberSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Member
#        load_instance = True

class CircularItemSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = CircularItem
#        include_fk = True

class CircularSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Circular
    items = ma.Nested(CircularItemSchema,many=True)
