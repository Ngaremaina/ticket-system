from flask import Blueprint, jsonify, request, session

from server.extensions import bcrypt, db
from server.models import Auth
from server.schemas import AuthSchema, LoginSchema

# Create a Blueprint for the authentication routes
auth = Blueprint("auth", __name__)

#Register user
@auth.route("/register", methods = ["POST"])
def add_users():
    #Validate the details from the user
    data = AuthSchema().load(request.get_json(silent=True) or {})
    email = data["email"].lower()

    #If the user exists return the message user exists
    if Auth.query.filter_by(email = email).first():
        return jsonify(message = "User exists"), 409

    #Hash the password and store it as text
    hashed_password = bcrypt.generate_password_hash(data["password"]).decode("utf-8")

    #Public sign ups are always clients; admins are created with `flask create-admin`
    new_user = Auth(email = email, password = hashed_password, role = "client")

    #Add user to the database
    db.session.add(new_user)
    db.session.commit()

    #Return the user details
    return jsonify({
        "id":new_user.id,
        "email":new_user.email
    }), 201


#Route for login user
@auth.route("/login", methods = ["POST"])
def login_user():
    #Validate the details from the user
    data = LoginSchema().load(request.get_json(silent=True) or {})

    #Check whether the user is in the database
    user = Auth.query.filter_by(email = data["email"].lower()).first()

    #If the user does not exist or the password is wrong return unauthorized
    if user is None or not bcrypt.check_password_hash(user.password, data["password"]):
        return jsonify(message = "Unauthorized"), 401

    #Create a fresh session to store the user id
    session.clear()
    session["user_id"] = user.id

    #Return the user details
    return jsonify({
        "id":user.id,
        "email": user.email,
        "role": user.role
    })

#Get details of the logged in user
@auth.route("/current_user", methods=["GET"])
def get_current_user():
    #Get the stored session by id
    user_id = session.get("user_id")
    user = db.session.get(Auth, user_id) if user_id else None

    #If invalid return the error message unauthorized
    if user is None:
        return jsonify(error = "Unauthorized"), 401

    #Return the user details
    return jsonify({
        "id": user.id,
        "email": user.email,
        "role": user.role
    })


#Route for logout
@auth.route("/logout", methods = ["POST"])
def logout_user():
    #Remove everything from the session
    session.clear()

    #Return the message logged out
    return jsonify("logged out"), 200
