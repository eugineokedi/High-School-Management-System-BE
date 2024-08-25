from api.models import db
from sqlalchemy_serializer import SerializerMixin

class Subject(db.Model, SerializerMixin):
  __tablename__ = 'subjects'

  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(100), nullable=False)
  description = db.Column(db.String(255), nullable=False)
  student_id = db.Column(db.Integer, db.ForeignKey('students.id'))

  # Relationships
  student = db.relationship('Student', back_populates='subjects')
  
  def __repr__(self):
    return f'<Subject id={self.id}, name={self.name}, description={self.description}>'