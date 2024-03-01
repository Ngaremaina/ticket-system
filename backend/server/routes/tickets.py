from server import *

# Create a Blueprint for the 'tickets' module
tickets = Blueprint('tickets', __name__)

#Get all the tickets
@tickets.route("/tickets", methods = ["GET"])
def get_tickets():
    #Query all the tickets from the database
    ticket_list = Ticket.query.all()

     # Serialize the data using TicketSchema and dump it
    ticket_data = TicketSchema(many = True).dump(ticket_list)

    # Return the serialized data as JSON
    return make_response(jsonify(ticket_data), 200)

#Get all the ticket details by id
@tickets.route("/tickets/<int:id>", methods = ["GET"])
def get_ticket(id):
    #Query the ticket by id from the database
    ticket = Ticket.query.filter_by(id =  id).first()

    # Serialize the data using TicketSchema and dump it
    ticket_data = TicketSchema().dump(ticket)

    # Return the serialized data as JSON
    return make_response(jsonify(ticket_data), 200)

#Route to add tickets to the database
@tickets.route("/tickets", methods = ["POST"])
def add_ticket():
     # Get the data from the request
    data = request.get_json()

    # Deserialize the data using TicketSchema and load it
    tickets = TicketSchema().load(data)

     # Create a new ticket object with the loaded data
    new_ticket = Ticket(**tickets)
    
     # Add the new ticket object to the database
    db.session.add(new_ticket)
    db.session.commit()

      # Serialize the data using TicketSchema and dump it
    ticket_schema = TicketSchema().dump(new_ticket)
    
     # Return the serialized data as JSON
    return make_response(jsonify(ticket_schema))

#Route to update tickets
@tickets.route('/tickets/<int:id>', methods=['PATCH'])
def update_ticket_details(id):
     #Query the data from the database by id
    ticket = Ticket.query.filter_by(id = id).first()

   # Get the new data from the request
    data = request.get_json()

    # Deserialize the data using TicketSchema and load it
    tickets = TicketSchema().load(data)

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
def delete_ticket(id):
    #Query the data from the database by id
    ticket = Ticket.query.filter_by(id = id).first()

     # Delete the Ticket object from the database
    db.session.delete(ticket)
    db.session.commit()

    # Return a success message
    return make_response(jsonify(message = "ticket deleted successfully"), 200)