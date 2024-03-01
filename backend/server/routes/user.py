from server import *

# Create a Blueprint for the 'user' module
user = Blueprint('user', __name__)

#Get all the users
@user.route("/users", methods = ["GET"])
def get_users():
    #Query all the users from the database
    users_list = Auth.query.all()

     # Serialize the data using AuthSchema and dump it
    user_data = AuthSchema(many = True).dump(users_list)  

    # Return the serialized data as JSON
    return make_response(jsonify(user_data), 200)

#Get all the user details by id
@user.route("/users/<int:id>", methods = ["GET"])
def get_users_by_id(id):
    #Query the user by id from the database
    users_list = Auth.query.filter_by(id = id).first()

    # Serialize the data using AuthSchema and dump it
    user_data = AuthSchema().dump(users_list)  

     # Return the serialized data as JSON
    return make_response(jsonify(user_data), 200)

#Route to update users
@user.route('/users/<int:id>', methods=['PATCH'])
def update_user_details(id):
     #Query the data from the database by id
    user = Auth.query.filter_by(id = id).first()

     # Get the new data from the request
    data = request.get_json()

   # Deserialize the data using AuthSchema and load it
    users = AuthSchema().load(data)

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
def delete_user(id):
    #Query the data from the database by id
    user = Auth.query.filter_by(id = id).first()

    # Delete the user object from the database
    db.session.delete(user)
    db.session.commit()
    
    # Return a success message
    return make_response(jsonify(message = "user deleted successfully"), 200)