from server import *

events = Blueprint('events', __name__)

@events.route("/events", methods = ["GET"])
def get_events():
    event_list = Event.query.all()
    event_data = EventSchema(many = True).dump(event_list)  
    return make_response(jsonify(event_data), 200)


@events.route("/events/<string:name>", methods = ["GET"])
def get_event(name):
    event = Event.query.filter_by(name = name).first()
    event_data = EventSchema().dump(event)
    return make_response(jsonify(event_data), 200)

@events.route("/events/<int:id>", methods = ["GET"])
def get_event_by_id(id):
    event = Event.query.filter_by(id = id).first()
    event_data = EventSchema().dump(event)
    return make_response(jsonify(event_data), 200)


@events.route("/events", methods = ["POST"])
def add_event():
    data = request.get_json()
    events = EventSchema().load(data)
    new_event = Event(**events)
    db.session.add(new_event)
    db.session.commit()
    event_schema = EventSchema().dump(new_event)
    return make_response(jsonify(event_schema))

@events.route('/events/<int:id>', methods=['PATCH'])
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

@events.route("/events/<int:id>", methods = ["DELETE"])
def delete_event(id):
    event = Event.query.filter_by(id = id).first()
    db.session.delete(event)
    db.session.commit()
    return make_response(jsonify(message = "event deleted successfully"), 200)