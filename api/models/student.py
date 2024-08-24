from api.models import db
from datetime import datetime, timezone

class Student(db.Model):
  __tablename__ = 'students'

  id = db.Column(db.Integer, primary_key=True)
  first_name = db.Column(db.String, nullable=False)
  last_name = db.Column(db.String, nullable=False)
  admission_number = db.Column(db.Integer, unique=True, nullable=False)
  date_of_birth = db.Column(db.Date, nullable=False)
  gender = db.Column(db.String, nullable=False)
  grade_level = db.Column(db.String, nullable=False)
  enrollment_date = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc) , nullable=False)
  user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

  def __repr__(self):
        return f'<Student id={self.id}, first_name={self.first_name}, last_name={self.last_name}, admission_number={self.admission_number}, grade_level={self.grade_level}, enrollment_date={self.enrollment_date}>'