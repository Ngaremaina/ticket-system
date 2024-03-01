from server import *

# Create a Blueprint for the 'events' module
events = Blueprint('events', __name__)

# Route to get all the events
@events.route("/events", methods = ["GET"])
def get_events():
    #Query all the events from the database
    event_list = Event.query.all()

     # Serialize the data using TypeSchema and dump it
    event_data = EventSchema(many = True).dump(event_list)  

     # Return the serialized data as JSON
    return make_response(jsonify(event_data), 200)

#Get all the event details by name
@events.route("/events/<string:name>", methods = ["GET"])
def get_event(name):
    #Query the event by name from the database
    event = Event.query.filter_by(name = name).first()

    # Serialize the data using EventSchema and dump it
    event_data = EventSchema().dump(event)

    # Return the serialized data as JSON
    return make_response(jsonify(event_data), 200)

#Get all the event details by id
@events.route("/events/<int:id>", methods = ["GET"])
def get_event_by_id(id):
     #Query the event by id from the database
    event = Event.query.filter_by(id = id).first()

    # Serialize the data using EventSchema and dump it
    event_data = EventSchema().dump(event)

     # Return the serialized data as JSON
    return make_response(jsonify(event_data), 200)

#Route to add events to the database
@events.route("/events", methods = ["POST"])
def add_event():
     # Get the new data from the request
    data = request.get_json()

    # Deserialize the data using EventSchema and load it
    events = EventSchema().load(data)

    # Create a new event object with the loaded data
    new_event = Event(**events)

    # Add the new event object to the database
    db.session.add(new_event)
    db.session.commit()

    # Serialize the data using EventSchema and dump it
    event_schema = EventSchema().dump(new_event)

     # Return the serialized data as JSON
    return make_response(jsonify(event_schema))

#Route to update events
@events.route('/events/<int:id>', methods=['PATCH'])
def update_event_details(id):

    #Query the data from the database by id
    event = Event.query.filter_by(id = id).first()

    # Get the new data from the request
    data = request.get_json()

    # Deserialize the data using EventSchema and load it
    events = EventSchema().load(data)

     # Update the Event object with the new data
    for field, value in events.items():
        setattr(event, field, value)

    # Commit the changes to the database
    db.session.add(event)
    db.session.commit() 

    # Serialize the data using EventSchema and dump it
    users_data = EventSchema().dump(event)

     # Return the serialized data as JSON
    return make_response(jsonify(users_data))

#Route to delete the events by Id
@events.route("/events/<int:id>", methods = ["DELETE"])
def delete_event(id):

    #Query the data from the database by id
    event = Event.query.filter_by(id = id).first()

    # Delete the Event object from the database
    db.session.delete(event)
    db.session.commit()

    # Return a success message
    return make_response(jsonify(message = "event deleted successfully"), 200)