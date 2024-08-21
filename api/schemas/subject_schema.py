from marshmallow import Schema, fields, validate

class SubjectSchema(Schema):
    id = fields.Int(dump_only=True)
    subject_name = fields.Str(required=True, validate=validate.Length(min=1))
    description = fields.Str(validate=validate.Length(max=255))
    teacher_id = fields.Int(required=True)
