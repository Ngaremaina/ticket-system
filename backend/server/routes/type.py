from server import *

# Create a Blueprint for the 'types' module
types = Blueprint('types', __name__)

# Route to get all the types
@types.route("/types", methods=["GET"])
def get_types():
    # Query all the types from the database
    type_list = Type.query.all()

    # Serialize the data using TypeSchema and dump it
    type_data = TypeSchema(many=True).dump(type_list)

    # Return the serialized data as JSON
    return make_response(jsonify(type_data), 200)

# Route to get type details by id
@types.route("/types/<int:id>", methods=["GET"])
def get_type(id):
    # Query the type by id from the database
    type = Type.query.filter_by(id=id).first()

    # Serialize the data using TypeSchema and dump it
    type_data = TypeSchema().dump(type)

    # Return the serialized data as JSON
    return make_response(jsonify(type_data), 200)

# Route to add types to the database
@types.route("/types", methods=["POST"])
def add_type():
    # Get the data from the request
    data = request.get_json()

    # Deserialize the data using TypeSchema and load it
    types = TypeSchema().load(data)

    # Create a new Type object with the loaded data
    new_type = Type(**types)

    # Add the new Type object to the database
    db.session.add(new_type)
    db.session.commit()

    # Serialize the data using TypeSchema and dump it
    type_schema = TypeSchema().dump(new_type)

    # Return the serialized data as JSON
    return make_response(jsonify(type_schema))

# Route to update types
@types.route('/types/<int:id>', methods=['PATCH'])
def update_type_details(id):
    # Query the data from the database by id
    type = Type.query.filter_by(id=id).first()

    # Get the new data from the request
    data = request.get_json()

    # Deserialize the data using TypeSchema and load it
    types = TypeSchema().load(data)

    # Update the Type object with the new data
    for field, value in types.items():
        setattr(type, field, value)

    # Commit the changes to the database
    db.session.add(type)
    db.session.commit()

    # Serialize the data using TypeSchema and dump it
    users_data = TypeSchema().dump(type)

    # Return the serialized data as JSON
    return make_response(jsonify(users_data))

# Route to delete the types by Id
@types.route("/types/<int:id>", methods=["DELETE"])
def delete_type(id):
    # Query the data from the database by id
    type = Type.query.filter_by(id=id).first()

    # Delete the Type object from the database
    db.session.delete(type)
    db.session.commit()

    # Return a success message
    return make_response(jsonify(message="Type deleted successfully"), 200)
