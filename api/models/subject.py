from api.models import db
from sqlalchemy_serializer import SerializerMixin

class Subject(db.Model, SerializerMixin):
  __tablename__ = 'subjects'

  id = db.Column(db.Integer, primary_key=True)
  subject_name = db.Column(db.String(100), nullable=False)
  description = db.Column(db.String(255), nullable=False)
  class_id = db.Column(db.Integer, db.ForeignKey('classes.id'), nullable=False)

  # Relationships
  classes = db.relationship('Class', back_populates='subjects')
  enrollments = db.relationship('Enrollment', back_populates='subject', cascade='all, delete-orphan')
  
  def __repr__(self):
    return f'<Subject id={self.id}, name={self.name}, description={self.description}>'