from server import *

types = Blueprint('types', __name__)

@types.route("/types", methods = ["GET"])
def get_types():
    type_list = Type.query.all()
    type_data = TypeSchema(many = True).dump(type_list)  
    return make_response(jsonify(type_data), 200)


@types.route("/types/<string:name>", methods = ["GET"])
def get_type(name):
    type = Type.query.filter_by(name = name).first()
    type_data = TypeSchema().dump(type)
    return make_response(jsonify(type_data), 200)


@types.route("/types", methods = ["POST"])
def add_type():
    data = request.get_json()
    types = TypeSchema().load(data)
    new_type = Type(**types)
    db.session.add(new_type)
    db.session.commit()
    type_schema = TypeSchema().dump(new_type)
    return make_response(jsonify(type_schema))

@types.route('/types/<int:id>', methods=['PATCH'])
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

@types.route("/types/<int:id>", methods = ["DELETE"])
def delete_type(id):
    type = Type.query.filter_by(id = id).first()
    db.session.delete(type)
    db.session.commit()
    return make_response(jsonify(message = "type deleted successfully"), 200)