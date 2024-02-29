from server import *

user = Blueprint('user', __name__)

@user.route("/users", methods = ["GET"])
def get_users():
    users_list = Auth.query.all()
    user_data = AuthSchema(many = True).dump(users_list)  
    return make_response(jsonify(user_data), 200)

@user.route("/users/<int:id>", methods = ["GET"])
def get_users_by_id(id):
    users_list = Auth.query.filter_by(id = id).first()
    user_data = AuthSchema().dump(users_list)  
    return make_response(jsonify(user_data), 200)

@user.route('/users/<int:id>', methods=['PATCH'])
def update_user_details(id):
    user = Auth.query.filter_by(id = id).first()
    data = request.get_json()
    users = AuthSchema().load(data)
    for field, value in users.items():
        setattr(user, field, value)
    db.session.add(user)
    db.session.commit() 

    users_data = AuthSchema().dump(user)
    return make_response(jsonify(users_data))

@user.route("/users/<int:id>", methods = ["DELETE"])
def delete_user(id):
    user = Auth.query.filter_by(id = id).first()
    db.session.delete(user)
    db.session.commit()
    return make_response(jsonify(message = "user deleted successfully"), 200)