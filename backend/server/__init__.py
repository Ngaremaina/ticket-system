#Import modules
from flask import Flask, make_response, jsonify, session, request, Blueprint
from server.models import *
from flask_bcrypt import Bcrypt
from flask_migrate import Migrate
from flask_session import Session
from flask_cors import CORS, cross_origin
import redis
from server.schemas import *
from datetime import datetime, timedelta, timezone
import json
from server.routes.events import events
from server.routes.user import user
from server.routes.tickets import tickets
from server.routes.type import types
from flask_mail import Mail, Message

# App Configuration
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://owen:Invest1gat1on@localhost/tickets" #Your account name, password and database name can be used
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'mainaowen1997@gmail.com'  # Your Gmail email address
app.config['MAIL_PASSWORD'] = ''  # Your Gmail password or app-specific password

#You can uncomment this if you have redis installed and configured
# SESSION_TYPE = "redis"
# SESSION_PERMANENT = False
# SESSION_USE_SIGNER = True
# SESSION_REDIS = redis.from_url("redis://127.0.0.1:6379")
# app.config.from_object(__name__)
# Session(app)

# Set a secret key
app.secret_key = b'\xaaA\xb0\x0c\x15\xad,`\xe6S\x82\x91\xcdv)\xe9'

#Create a database and migrate the schemas to the db
migrate = Migrate(app, db)

#Initialize the authentication library in the application
bcrypt = Bcrypt(app)

#Initialize the mail library
mail = Mail(app)

#Initialize the db 
db.init_app(app)

#Implement CORS
CORS(app, supports_credentials=True)

#Register all the applications 
app.register_blueprint(events)
app.register_blueprint(tickets)
app.register_blueprint(types)
app.register_blueprint(user)