from marshmallow import Schema, fields, validate

class GradeSchema(Schema):
    id = fields.Int(dump_only=True)
    student_id = fields.Int(required=True)
    subject_id = fields.Int(required=True)
    grade = fields.Str(required=True, validate=validate.Length(min=1, max=2))  # Example grades: A+, B, etc.
