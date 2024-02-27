from marshmallow import Schema, fields

class TypeSchema(Schema):
    name = fields.String()
    price = fields.Integer()
    event_id = fields.Integer()
    
class EventSchema(Schema):
    name = fields.String()
    description = fields.String()
    image = fields.String()
    max_attendees = fields.Integer()

    type = fields.Nested(TypeSchema, many = True)
