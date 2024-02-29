from flask_sqlalchemy import SQLAlchemy
from uuid import uuid4

db = SQLAlchemy()

class Auth(db.Model):
    __tablename__ = "auth"

    id = db.Column(db.Integer, primary_key = True, autoincrement=True)
    email = db.Column(db.String(255), nullable = False)
    password = db.Column(db.String(255), nullable = False)
    role = db.Column(db.String(255), nullable = False)
    

class Profile(db.Model):
    __tablename__ = "profile"

    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    firstname = db.Column(db.String(255), nullable = False)
    lastname = db.Column(db.String(255), nullable = False)

    auth_id = db.Column(db.Integer, db.ForeignKey('auth.id'), nullable = False)

    auth = db.relationship("Auth", backref = "profile")

class Event(db.Model):
    __tablename__ = "event"

    id = db.Column(db.Integer, primary_key=True, autoincrement = True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(100), nullable=False)
    venue = db.Column(db.String(100), nullable=False)
    date = db.Column(db.String(100), nullable=False)
    time = db.Column(db.String(100), nullable=False)
    image = db.Column(db.String(100), nullable=False)
    max_attendees = db.Column(db.Integer, nullable=False)

class Type(db.Model):
    __tablename__ = "type"

    id = db.Column(db.Integer, primary_key=True, autoincrement = True)
    name = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Integer, nullable = False)
    event_id = db.Column(db.Integer, db.ForeignKey('event.id'), nullable=False)

    event = db.relationship("Event", backref = "type")


class Ticket(db.Model):
    __tablename__ = "ticket"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(100), nullable=False)
    venue = db.Column(db.String(100), nullable=False)
    date = db.Column(db.String(100), nullable=False)
    time = db.Column(db.String(100), nullable=False)
    image = db.Column(db.String(100), nullable=False)
    persons = db.Column(db.Integer, nullable=False)
    type_name = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Integer, nullable = False)
    
    auth_id = db.Column(db.Integer, db.ForeignKey('auth.id'), nullable=False) 
    auth = db.relationship("Auth", backref = "ticket")