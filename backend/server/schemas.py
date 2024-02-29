from marshmallow import Schema, fields

class TicketSchema(Schema):
    id = fields.Integer()
    name = fields.String()
    description = fields.String()
    venue = fields.String()
    date = fields.String()
    time = fields.String()
    image = fields.String()
    persons = fields.Integer()
    type_name = fields.String()
    price = fields.Integer()
    auth_id = fields.Integer()

class TypeSchema(Schema):
    id = fields.Integer()
    name = fields.String()
    price = fields.Integer()
    event_id = fields.Integer()

    # ticket = fields.Nested(TicketSchema, many=True)
    
class EventSchema(Schema):
    id = fields.Integer()
    name = fields.String()
    description = fields.String()
    image = fields.String()
    date = fields.String()
    time = fields.String()
    venue = fields.String()
    max_attendees = fields.Integer()
    auth_id = fields.Integer()

    type = fields.Nested(TypeSchema, many = True)

class AuthSchema(Schema):
    id = fields.Integer()
    email = fields.String()
    password = fields.String()
    role = fields.String()

    ticket = fields.Nested(TicketSchema, many=True)

