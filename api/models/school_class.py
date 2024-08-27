from api.models import db
from sqlalchemy_serializer import SerializerMixin

class Class(db.Model, SerializerMixin):
  __tablename__ = 'classes'

  id = db.Column(db.Integer, primary_key=True)
  class_name = db.Column(db.String(100), nullable=False)
  teacher_id = db.Column(db.Integer, db.ForeignKey('teachers.id'), nullable=False)

  # Relationships
  teachers = db.relationship('Teacher', back_populates='classes')
  enrollments = db.relationship('Enrollment', back_populates='classes', cascade='all, delete-orphan')
  attendance = db.relationship('Attendance', back_populates='classes', cascade='all, delete-orphan')
  grades = db.relationship('Grade', back_populates='classes', cascade='all, delete-orphan')
  class_schedules = db.relationship('ClassSchedule', back_populates='classes', cascade='all, delete-orphan')
  subjects = db.relationship('Subject', back_populates='classes', cascade='all, delete-orphan')

  def __repr__(self):
    return f'<Class id={self.id}, class_name={self.class_name}, subject={self.subject}>'