from flask import Flask, make_response, jsonify, session
from models import *
from flask_bcrypt import Bcrypt
from flask_migrate import Migrate
from flask_session import Session

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///app.db"
app.secret_key = "b'\x01j4\xb3|}\x1f\x19\xa0\xba\x81\xfb\x18\x03\x9f\x83'"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False


migrate = Migrate(app, db)
bcrypt = Bcrypt(app)

db.init_app(app)
server_session = Session(app)

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

    return make_response(jsonify(new_user))

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

    return jsonify(user)

@app.route("/current_user")
def get_current_user():
    user_id = session.get("user_id")

    if not user_id:
        return jsonify(error =  "Unauthorized")

    user = Auth.query.filter_by(id = user_id).first()
    return jsonify({
        "id":user.id,
        "email":user.email
    })
if __name__ == "__main__":
    app.run(debug=True)