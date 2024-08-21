from . import db
from datetime import datetime, timezone

class Teacher(db.Model):
  __tablename__ = 'teachers'

  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String, nullable=False)
  subject = db.Column(db.String, nullable=False)
  hire_date = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc), nullable=False)
  qualification = db.Column(db.String, nullable=False)

  def __repr__(self):
      return f'<Teacher id={self.id}, name={self.name}, subject={self.subject}, hire_date={self.hire_date}, qualification={self.qualification}>'