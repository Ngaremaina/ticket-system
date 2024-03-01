#import flask sqlalchemy
from flask_sqlalchemy import SQLAlchemy

# Initialize SQLAlchemy to interact with the database
db = SQLAlchemy()

# Define a SQLAlchemy model named "Auth" to represent the users in the database.
class Auth(db.Model):
    __tablename__ = "auth"

    id = db.Column(db.Integer, primary_key = True, autoincrement=True)
    email = db.Column(db.String(255), nullable = False)
    password = db.Column(db.String(255), nullable = False)
    role = db.Column(db.String(255), nullable = False)
    
# Define a SQLAlchemy model named "Profile" to represent profiles of the users in the database.
class Profile(db.Model):
    __tablename__ = "profile"

    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    firstname = db.Column(db.String(255), nullable = False)
    lastname = db.Column(db.String(255), nullable = False)

    #Define a foreign key relationship to the 'id' column of the 'auth' table,
    # ensuring that each 'auth_id' value references an existing 'id' in the 'auth' table.
    auth_id = db.Column(db.Integer, db.ForeignKey('auth.id'), nullable = False)

    # Establishes a one-to-one relationship between the "Auth" and "Profile" models,
    # allowing easy access to the related "Auth" instance(s) associated with a "Profile" instance
    # via the "profile" attribute of the "Auth" model.

    auth = db.relationship("Auth", backref = "profile")

# Define a SQLAlchemy model named "Event" to represent events in the database.
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

# Define a SQLAlchemy model named "Type" to represent type of ticket ie VIP or Regular in the database.
class Type(db.Model):
    __tablename__ = "type"

    id = db.Column(db.Integer, primary_key=True, autoincrement = True)
    name = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Integer, nullable = False)

    #Define a foreign key relationship to the 'id' column of the 'event' table,
    # ensuring that each 'event_id' value references an existing 'id' in the 'event' table.
    event_id = db.Column(db.Integer, db.ForeignKey('event.id'), nullable=False)

    # Establishes a one-to-many relationship between the "Event" and "Type" models,
    # allowing easy access to the related "Event" instance(s) associated with a "Type" instance
    # via the "type" attribute of the "Event" model.
    event = db.relationship("Event", backref = "type")

# Define a SQLAlchemy model named "Ticket" to represent tickets booked by each user in the database.
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
    
    #Define a foreign key relationship to the 'id' column of the 'auth' table,
    # ensuring that each 'aith_id' value references an existing 'id' in the 'auth' table.
    auth_id = db.Column(db.Integer, db.ForeignKey('auth.id'), nullable=False) 

    # Establishes a one-to-many relationship between the "Auth" and "Ticket" models,
    # allowing easy access to the related "Auth" instance(s) associated with a "Ticket" instance
    # via the "ticket" attribute of the "Auth" model.
    auth = db.relationship("Auth", backref = "ticket")