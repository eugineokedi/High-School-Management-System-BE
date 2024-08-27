from api.models import db
import enum
from sqlalchemy_serializer import SerializerMixin

class GradeEnum(enum.Enum):
    A = 'A'
    A_minus = 'A-'
    B_plus = 'B+'
    B = 'B'
    B_minus = 'B-'
    C_plus = 'C+'
    C = 'C'
    C_minus = 'C-'
    D_plus = 'D+'
    D = 'D'
    D_minus = 'D-'
    F = 'F'
    X = 'X'
    Y = 'Y'
    Z = 'Z'

class Enrollment(db.Model, SerializerMixin):
    __tablename__ = 'enrollments'

    id = db.Column(db.Integer, primary_key=True)
    enrollment_date = db.Column(db.Date, nullable=False)
    grade = db.Column(db.Enum(GradeEnum), nullable=False)
    class_id = db.Column(db.Integer, db.ForeignKey('classes.id'), nullable=False)
    student_id = db.Column(db.Integer, db.ForeignKey('students.id'), nullable=False)
    subject_id = db.Column(db.Integer, db.ForeignKey('subjects.id'), nullable=False)

    # Relationships
    student = db.relationship('Student', back_populates='enrollments')
    classes = db.relationship('Class', back_populates='enrollments')
    subject = db.relationship('Subject', back_populates='enrollments')

    def __repr__(self):
        return f'<Enrollment id={self.id}, enrollment_date={self.enrollment_date}, grade={self.grade.value}>'
