from api.models import db
from datetime import datetime, timezone
from sqlalchemy_serializer import SerializerMixin

class Teacher(db.Model, SerializerMixin):
  __tablename__ = 'teachers'

  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(100), nullable=False)
  subject = db.Column(db.String(50), nullable=False)
  hire_date = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc), nullable=False)
  qualification = db.Column(db.String, nullable=False)
  user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

  # Relationships
  classes = db.relationship('Class', back_populates='teacher', cascade='all, delete-orphan')

  def __repr__(self):
      return f'<Teacher id={self.id}, name={self.name}, subject={self.subject}, hire_date={self.hire_date}, qualification={self.qualification}>'