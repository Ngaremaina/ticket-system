from marshmallow import Schema, fields

class TypeSchema(Schema):
    id = fields.Integer()
    name = fields.String()
    price = fields.Integer()
    event_id = fields.Integer()
    
class EventSchema(Schema):
    id = fields.Integer()
    name = fields.String()
    description = fields.String()
    image = fields.String()
    date = fields.String()
    time = fields.String()
    venue = fields.String()
    max_attendees = fields.Integer()

    type = fields.Nested(TypeSchema, many = True)
