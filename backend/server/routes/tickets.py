from server import *

tickets = Blueprint('tickets', __name__)


@tickets.route("/tickets", methods = ["GET"])
def get_tickets():
    ticket_list = Ticket.query.all()
    ticket_data = TicketSchema(many = True).dump(ticket_list)  
    return make_response(jsonify(ticket_data), 200)

@tickets.route("/tickets/<int:id>", methods = ["GET"])
def get_ticket(id):
    ticket = Ticket.query.filter_by(id =  id).first()
    ticket_data = TypeSchema().dump(ticket)
    return make_response(jsonify(ticket_data), 200)

@tickets.route("/tickets", methods = ["POST"])
def add_ticket():
    data = request.get_json()
    tickets = TicketSchema().load(data)
    new_ticket = Ticket(**tickets)
    db.session.add(new_ticket)
    db.session.commit()
    type_schema = TypeSchema().dump(new_ticket)
    return make_response(jsonify(type_schema))

@tickets.route('/tickets/<int:id>', methods=['PATCH'])
def update_ticket_details(id):
    ticket = Ticket.query.filter_by(id = id).first()
    data = request.get_json()
    tickets = TicketSchema().load(data)
    for field, value in tickets.items():
        setattr(ticket, field, value)
    db.session.add(ticket)
    db.session.commit() 

    users_data = TypeSchema().dump(ticket)
    return make_response(jsonify(users_data))

@tickets.route("/tickets/<int:id>", methods = ["DELETE"])
def delete_ticket(id):
    ticket = Ticket.query.filter_by(id = id).first()
    db.session.delete(ticket)
    db.session.commit()
    return make_response(jsonify(message = "ticket deleted successfully"), 200)