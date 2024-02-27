from flask import Flask, make_response, jsonify, session, request
from models import *
from flask_bcrypt import Bcrypt
from flask_migrate import Migrate
from flask_session import Session
from flask_cors import CORS
import redis
from schemas import *

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///app.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

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

db.init_app(app)

CORS(app, supports_credentials=True)

@app.route("/register", methods = ["POST"])
def add_users():
    email = request.json["email"]
    password = request.json["password"]
    role = request.json["role"]

    user_exists = Auth.query.filter_by(email = email).first()

    if user_exists:
        return jsonify(message = "User exists")

    hashed_password = bcrypt.generate_password_hash(password)

    new_user = Auth(email = email, password = hashed_password, role = role)
    db.session.add(new_user)
    db.session.commit()

    return jsonify({
        "id":new_user.id,
        "email":new_user.email
    })

@app.route("/login", methods = ["POST"])
def login_user():
    email = request.json["email"]
    password = request.json["password"]

    user = Auth.query.filter_by(email = email).first()

    session["user_id"] = user.id

    if user is None:
        return jsonify(message = "Unauthorized")

    if not bcrypt.check_password_hash(user.password, password):
        return jsonify(message = "Unauthorized")

    return jsonify({
        "id":user.id,
        "email":user.email
    })

@app.route("/current_user")
def get_current_user():
    user_id = session.get("user_id")

    if not user_id:
        return jsonify(error =  "Unauthorized")

    user = Auth.query.filter_by(id = user_id).first()
    return jsonify({
        "id":user.id,
        "email":user.email,
        "role":user.role
    })


@app.route("/logout", methods = ["POST"])
def logout_user():
    session.pop("user_id")
    return make_response(jsonify("logged out"), 200)


@app.route("/events", methods = ["GET"])
def get_events():
    event_list = Event.query.all()
    event_data = EventSchema(many = True).dump(event_list)  
    return make_response(jsonify(event_data), 200)


@app.route("/events/<string:name>", methods = ["GET"])
def get_event(name):
    event = Event.query.filter_by(name = name).first()
    event_data = EventSchema().dump(event)
    return make_response(jsonify(event_data), 200)


@app.route("/events", methods = ["POST"])
def add_event():
    data = request.get_json()
    events = EventSchema().load(data)
    new_event = Event(**events)
    db.session.add(new_event)
    db.session.commit()
    event_schema = EventSchema().dump(new_event)
    return make_response(jsonify(event_schema))

@app.route('/events/<int:id>', methods=['PATCH'])
def update_event_details(id):
    event = Event.query.filter_by(id = id).first()
    data = request.get_json()
    events = EventSchema().load(data)
    for field, value in events.items():
        setattr(event, field, value)
    db.session.add(event)
    db.session.commit() 

    users_data = EventSchema().dump(event)
    return make_response(jsonify(users_data))

@app.route("/events/<int:id>", methods = ["DELETE"])
def delete_event(id):
    event = Event.query.filter_by(id = id).first()
    db.session.delete(event)
    db.session.commit()
    return make_response(jsonify(message = "event deleted successfully"), 200)


@app.route("/types", methods = ["GET"])
def get_types():
    type_list = Type.query.all()
    type_data = TypeSchema(many = True).dump(type_list)  
    return make_response(jsonify(type_data), 200)


@app.route("/types/<string:name>", methods = ["GET"])
def get_type(name):
    type = Type.query.filter_by(name = name).first()
    type_data = TypeSchema().dump(type)
    return make_response(jsonify(type_data), 200)


@app.route("/types", methods = ["POST"])
def add_type():
    data = request.get_json()
    types = TypeSchema().load(data)
    new_type = Type(**types)
    db.session.add(new_type)
    db.session.commit()
    type_schema = TypeSchema().dump(new_type)
    return make_response(jsonify(type_schema))

@app.route('/types/<int:id>', methods=['PATCH'])
def update_type_details(id):
    type = Type.query.filter_by(id = id).first()
    data = request.get_json()
    types = TypeSchema().load(data)
    for field, value in types.items():
        setattr(type, field, value)
    db.session.add(type)
    db.session.commit() 

    users_data = TypeSchema().dump(type)
    return make_response(jsonify(users_data))

@app.route("/types/<int:id>", methods = ["DELETE"])
def delete_type(id):
    type = Type.query.filter_by(id = id).first()
    db.session.delete(type)
    db.session.commit()
    return make_response(jsonify(message = "type deleted successfully"), 200)

if __name__ == "__main__":
    app.run(debug=True)