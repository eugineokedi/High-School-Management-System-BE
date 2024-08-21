from marshmallow import Schema, fields, validate

class AttendanceSchema(Schema):
    id = fields.Int(dump_only=True)
    student_id = fields.Int(required=True)
    date = fields.Date(required=True)
    status = fields.Str(required=True, validate=validate.OneOf(["Present", "Absent", "Late"]))
