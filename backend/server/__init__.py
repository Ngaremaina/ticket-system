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


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+mysqlconnector://owen:Invest1gat1on@localhost/tickets"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(hours=1)
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'mainangare85@gmail.com'  # Your Gmail email address
app.config['MAIL_PASSWORD'] = 'Ng@re@2123'  # Your Gmail password or app-specific password


SESSION_TYPE = "redis"
SESSION_PERMANENT = False
SESSION_USE_SIGNER = True
SESSION_REDIS = redis.from_url("redis://127.0.0.1:6379")
app.config.from_object(__name__)
Session(app)

# Set a secret key
app.secret_key = 'your_secret_key_here'

migrate = Migrate(app, db)
bcrypt = Bcrypt(app)
mail = Mail(app)

db.init_app(app)

jwt = JWTManager(app)

CORS(app, supports_credentials=True)


app.register_blueprint(events)
app.register_blueprint(tickets)
app.register_blueprint(types)
app.register_blueprint(user)