from api.models import db
from sqlalchemy_serializer import SerializerMixin

class Class(db.Model, SerializerMixin):
  __tablename__ = 'classes'

  id = db.Column(db.Integer, primary_key=True)
  class_name = db.Column(db.String(100), nullable=False)
  subject = db.Column(db.String(100), nullable=False)
  schedule = db.Column(db.String(255), nullable=False)
  teacher_id = db.Column(db.Integer, db.ForeignKey('teacher.id'))

  # Relationships
  teacher = db.relationship('Teacher', back_populates='classes')
  enrollments = db.relationship('Enrollment', back_populates='class', cascade='all, delete-orphan')
  attendance = db.relationship('Attendance', back_populates='class', cascade='all, delete-orphan')
  grades = db.relationship('Grade', back_populates='class', cascade='all, delete-orphan')
  class_schedule = db.relationship('ClassSchedule', back_populates='class', cascade='all, delete-orphan')

  def __repr__(self):
    return f'<Class id={self.id}, class_name={self.class_name}, subject={self.subject}, schedule={self.schedule}>'