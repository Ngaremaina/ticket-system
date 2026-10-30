from flask import Blueprint, jsonify, make_response, request

from server.authentication import admin_required, login_required, require_self_or_admin
from server.extensions import bcrypt, db
from server.models import Auth
from server.schemas import AuthSchema

# Create a Blueprint for the 'user' module
user = Blueprint('user', __name__)

#Get all the users
@user.route("/users", methods = ["GET"])
@admin_required
def get_users():
    #Query all the users from the database
    users_list = Auth.query.all()

     # Serialize the data using AuthSchema and dump it
    user_data = AuthSchema(many = True).dump(users_list)  

    # Return the serialized data as JSON
    return make_response(jsonify(user_data), 200)

#Get all the user details by id
@user.route("/users/<int:id>", methods = ["GET"])
@login_required
def get_users_by_id(id):
    #Users can only view their own profile unless they are an admin
    require_self_or_admin(id)

    #Query the user by id from the database
    users_list = db.get_or_404(Auth, id)

    # Serialize the data using AuthSchema and dump it
    user_data = AuthSchema().dump(users_list)  

     # Return the serialized data as JSON
    return make_response(jsonify(user_data), 200)

#Route to update users
@user.route('/users/<int:id>', methods=['PATCH'])
@login_required
def update_user_details(id):
    #Users can only update their own profile unless they are an admin
    require_self_or_admin(id)

     #Query the data from the database by id
    user = db.get_or_404(Auth, id)

     # Get the new data from the request
    data = request.get_json(silent=True) or {}

   # Deserialize the data using AuthSchema and load it
    users = AuthSchema(partial=True).load(data)

    # Emails must stay unique
    if "email" in users:
        users["email"] = users["email"].lower()
        if Auth.query.filter(Auth.email == users["email"], Auth.id != id).first():
            return make_response(jsonify(message = "User exists"), 409)

    # Never store a plain text password
    if "password" in users:
        users["password"] = bcrypt.generate_password_hash(users["password"]).decode("utf-8")

    # Update the users object with the new data
    for field, value in users.items():
        setattr(user, field, value)

    # Commit the changes to the database
    db.session.add(user)
    db.session.commit() 

    # Serialize the data using AuthSchema and dump it
    users_data = AuthSchema().dump(user)

      # Return the serialized data as JSON
    return make_response(jsonify(users_data))

#Route to delete the users by Id
@user.route("/users/<int:id>", methods = ["DELETE"])
@admin_required
def delete_user(id):
    #Query the data from the database by id
    user = db.get_or_404(Auth, id)

    # Delete the user object from the database
    db.session.delete(user)
    db.session.commit()
    
    # Return a success message
    return make_response(jsonify(message = "user deleted successfully"), 200)