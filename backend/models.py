from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Auth(db.Model):
    __tablename__ = "auth"

    id = db.Column(db.Integer, primary_key = True, autoincrement=True)
    email = db.Column(db.String(255), nullable = False)
    password = db.Column(db.String(255), nullable = False)
    role = db.Column(db.String(255), nullable = False)

