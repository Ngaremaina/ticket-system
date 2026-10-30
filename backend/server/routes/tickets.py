from flask import Blueprint, abort, jsonify, make_response, request

from server.authentication import admin_required, current_user, login_required, require_self_or_admin
from server.extensions import db
from server.models import Ticket
from server.schemas import TicketSchema

# Create a Blueprint for the 'tickets' module
tickets = Blueprint('tickets', __name__)

# Maximum number of tickets a single user can book
MAX_TICKETS_PER_USER = 5

#Get all the tickets (admins see every ticket, clients only their own)
@tickets.route("/tickets", methods = ["GET"])
@login_required
def get_tickets():
    user = current_user()
    query = Ticket.query if user.role == "admin" else Ticket.query.filter_by(auth_id = user.id)
    ticket_list = query.all()

     # Serialize the data using TicketSchema and dump it
    ticket_data = TicketSchema(many = True).dump(ticket_list)

    # Return the serialized data as JSON
    return make_response(jsonify(ticket_data), 200)

#Get all the ticket details by id
@tickets.route("/tickets/<int:id>", methods = ["GET"])
@login_required
def get_ticket(id):
    #Query the ticket by id from the database
    ticket = db.get_or_404(Ticket, id)
    require_self_or_admin(ticket.auth_id)

    # Serialize the data using TicketSchema and dump it
    ticket_data = TicketSchema().dump(ticket)

    # Return the serialized data as JSON
    return make_response(jsonify(ticket_data), 200)

#Route to add tickets to the database
@tickets.route("/tickets", methods = ["POST"])
@login_required
def add_ticket():
     # Get the data from the request
    data = request.get_json(silent=True) or {}

    # Deserialize the data using TicketSchema and load it
    tickets = TicketSchema().load(data)

    #Tickets always belong to the logged in user
    user = current_user()
    if Ticket.query.filter_by(auth_id = user.id).count() >= MAX_TICKETS_PER_USER:
        abort(400, description = f"You can book at most {MAX_TICKETS_PER_USER} tickets")

     # Create a new ticket object with the loaded data
    new_ticket = Ticket(**tickets, auth_id = user.id)
    
     # Add the new ticket object to the database
    db.session.add(new_ticket)
    db.session.commit()

      # Serialize the data using TicketSchema and dump it
    ticket_schema = TicketSchema().dump(new_ticket)
    
     # Return the serialized data as JSON
    return make_response(jsonify(ticket_schema), 201)

#Route to update tickets
@tickets.route('/tickets/<int:id>', methods=['PATCH'])
@admin_required
def update_ticket_details(id):
     #Query the data from the database by id
    ticket = db.get_or_404(Ticket, id)

   # Get the new data from the request
    data = request.get_json(silent=True) or {}

    # Deserialize the data using TicketSchema and load it
    tickets = TicketSchema(partial=True).load(data)

     # Update the ticket object with the new data
    for field, value in tickets.items():
        setattr(ticket, field, value)

    # Commit the changes to the database
    db.session.add(ticket)
    db.session.commit() 

    # Serialize the data using TicketSchema and dump it
    ticket_data = TicketSchema().dump(ticket)

     # Return the serialized data as JSON
    return make_response(jsonify(ticket_data))

#Route to delete the tickets by Id
@tickets.route("/tickets/<int:id>", methods = ["DELETE"])
@login_required
def delete_ticket(id):
    #Query the data from the database by id
    ticket = db.get_or_404(Ticket, id)
    #Clients can only cancel their own tickets
    require_self_or_admin(ticket.auth_id)

     # Delete the Ticket object from the database
    db.session.delete(ticket)
    db.session.commit()

    # Return a success message
    return make_response(jsonify(message = "ticket deleted successfully"), 200)