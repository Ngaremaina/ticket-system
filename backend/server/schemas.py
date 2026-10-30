from marshmallow import EXCLUDE, Schema, fields, validate


# Base schema: silently drop fields the API does not know about instead of failing
class BaseSchema(Schema):
    class Meta:
        unknown = EXCLUDE


# Schema for representing Ticket objects
class TicketSchema(BaseSchema):
    id = fields.Integer(dump_only=True)  # Ticket ID
    name = fields.String(required=True)  # Ticket name
    description = fields.String(required=True)  # Ticket description
    venue = fields.String(required=True)  # Venue of the event
    date = fields.String(required=True)  # Date of the event
    time = fields.String(required=True)  # Time of the event
    image = fields.String(required=True)  # URL of the ticket image
    persons = fields.Integer(required=True, validate=validate.Range(min=1))  # Number of persons allowed per ticket
    type_name = fields.String(required=True)  # Type of the ticket
    price = fields.Integer(required=True, validate=validate.Range(min=0))  # Price of the ticket
    auth_id = fields.Integer(required=True)  # ID of the authentication associated with the ticket

# Schema for representing Type objects
class TypeSchema(BaseSchema):
    id = fields.Integer(dump_only=True)  # Type ID
    name = fields.String(required=True)  # Type name
    price = fields.Integer(required=True, validate=validate.Range(min=0))  # Price of the type
    event_id = fields.Integer(required=True)  # ID of the event associated with the type

# Schema for representing Event objects
class EventSchema(BaseSchema):
    id = fields.Integer(dump_only=True)  # Event ID
    name = fields.String(required=True)  # Event name
    description = fields.String(required=True)  # Event description
    image = fields.String(required=True)  # URL of the event image
    date = fields.String(required=True)  # Date of the event
    time = fields.String(required=True)  # Time of the event
    venue = fields.String(required=True)  # Venue of the event
    max_attendees = fields.Integer(required=True, validate=validate.Range(min=0))  # Maximum number of attendees for the event
    type = fields.Nested(TypeSchema, many=True, dump_only=True)  # Types associated with the event

# Schema for representing Auth objects
class AuthSchema(BaseSchema):
    id = fields.Integer(dump_only=True)  # Auth ID
    email = fields.Email(required=True)  # Email of the user
    password = fields.String(required=True, load_only=True, validate=validate.Length(min=6))  # Password of the user (never returned)
    role = fields.String(dump_only=True)  # Role of the user (only changeable via the create-admin CLI)
    ticket = fields.Nested(TicketSchema, many=True, dump_only=True)  # Tickets associated with the authentication

# Schema for validating login requests
class LoginSchema(BaseSchema):
    email = fields.Email(required=True)
    password = fields.String(required=True, load_only=True)
