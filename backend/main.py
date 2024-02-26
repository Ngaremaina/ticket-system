from flask import Flask, make_response, jsonify, session, request
from models import *
from flask_bcrypt import Bcrypt
from flask_migrate import Migrate
from flask_session import Session
import redis

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

if __name__ == "__main__":
    app.run(debug=True)