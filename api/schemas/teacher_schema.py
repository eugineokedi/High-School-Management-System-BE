from marshmallow import Schema, fields, validate

class TeacherSchema(Schema):
    id = fields.Int(dump_only=True)
    first_name = fields.Str(required=True, validate=validate.Length(min=1))
    last_name = fields.Str(required=True, validate=validate.Length(min=1))
    email = fields.Email(required=True)
    subject = fields.List(fields.Int(), dump_only=True)  # List of course IDs the teacher manages
