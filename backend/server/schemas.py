from marshmallow import Schema, fields

# Schema for representing Ticket objects
class TicketSchema(Schema):
    id = fields.Integer()  # Ticket ID
    name = fields.String()  # Ticket name
    description = fields.String()  # Ticket description
    venue = fields.String()  # Venue of the event
    date = fields.String()  # Date of the event
    time = fields.String()  # Time of the event
    image = fields.String()  # URL of the ticket image
    persons = fields.Integer()  # Number of persons allowed per ticket
    type_name = fields.String()  # Type of the ticket
    price = fields.Integer()  # Price of the ticket
    auth_id = fields.Integer()  # ID of the authentication associated with the ticket

# Schema for representing Type objects
class TypeSchema(Schema):
    id = fields.Integer()  # Type ID
    name = fields.String()  # Type name
    price = fields.Integer()  # Price of the type
    event_id = fields.Integer()  # ID of the event associated with the type
    # ticket = fields.Nested(TicketSchema, many=True)  # Optional: Relationship with Ticket objects

# Schema for representing Event objects
class EventSchema(Schema):
    id = fields.Integer()  # Event ID
    name = fields.String()  # Event name
    description = fields.String()  # Event description
    image = fields.String()  # URL of the event image
    date = fields.String()  # Date of the event
    time = fields.String()  # Time of the event
    venue = fields.String()  # Venue of the event
    max_attendees = fields.Integer()  # Maximum number of attendees for the event
    auth_id = fields.Integer()  # ID of the authentication associated with the event
    type = fields.Nested(TypeSchema, many=True)  # Types associated with the event

# Schema for representing Auth objects
class AuthSchema(Schema):
    id = fields.Integer()  # Auth ID
    email = fields.String()  # Email of the user
    password = fields.String()  # Password of the user
    role = fields.String()  # Role of the user
    ticket = fields.Nested(TicketSchema, many=True)  # Tickets associated with the authentication
