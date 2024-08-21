from marshmallow import Schema, fields, validate

class StudentSchema(Schema):
    id = fields.Int(dump_only=True)
    first_name = fields.Str(required=True, validate=validate.Length(min=1))
    last_name = fields.Str(required=True, validate=validate.Length(min=1))
    date_of_birth = fields.Date(required=True)
    email = fields.Email(required=True)
    subject = fields.List(fields.Int(), dump_only=True)  # List of course IDs the student is enrolled in
