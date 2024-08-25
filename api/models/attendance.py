from api.models import db
import enum
from sqlalchemy_serializer import SerializerMixin

class StatusEnum(enum.Enum):
    present = 'present'
    absent = 'absent'
    late = 'late'

class Attendance(db.Model, SerializerMixin):
    __tablename__ = 'attendances'

    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date, nullable=False)
    status = db.Column(db.Enum(StatusEnum), nullable=False)
    student_id = db.Column(db.Integer, db.ForeignKey('students.id'), nullable=False)
    class_id = db.Column(db.Integer, db.ForeignKey('classes.id'), nullable=False)

    # Relationships
    student = db.relationship('Student', back_populates='attendance')
    classes = db.relationship('Class', back_populates='attendance')

    def __repr__(self):
        return f'<Attendance id={self.id}, date={self.date}, status={self.status.value}>'
