from api.models import db
from datetime import datetime, timezone
from sqlalchemy_serializer import SerializerMixin

class Student(db.Model, SerializerMixin):
  __tablename__ = 'students'

  id = db.Column(db.Integer, primary_key=True)
  first_name = db.Column(db.String, nullable=False)
  last_name = db.Column(db.String, nullable=False)
  admission_number = db.Column(db.Integer, unique=True, nullable=False)
  date_of_birth = db.Column(db.Date, nullable=False)
  gender = db.Column(db.String(10), nullable=False)
  grade_level = db.Column(db.String(10), nullable=False)
  enrollment_date = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc) , nullable=False)
  user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
  parent_id = db.Column(db.Integer, db.ForeignKey('parents.id'), nullable=False)
  event_id = db.Column(db.Integer, db.ForeignKey('events.id'), nullable=False)

  # Relationships
  parent = db.relationship('Parent', back_populates='students')
  enrollments = db.relationship('Enrollment', back_populates='students', cascade='all, delete-orphan')
  book_loans = db.relationship('BookLoan', back_populates='student', cascade='all, delete-orphan')
  payments = db.relationship('Payment', back_populates='student', cascade='all, delete-orphan')
  attendance = db.relationship('Attendance', back_populates='student', cascade='all, delete-orphan')
  grades = db.relationship('Grade', back_populates='student', cascade='all, delete-orphan')
  discipline_records = db.relationship('DisciplineRecord', back_populates='student', cascade='all, delete-orphan')
  subjects = db.relationship('Subject', back_populates='subject', cascade='all, delete-orphan')
  events = db.relationship('Event', back_populates='student')

  # Serialize rules
  serialize_rules = ('-parent', '-event', )


  def __repr__(self):
        return f'<Student id={self.id}, first_name={self.first_name}, last_name={self.last_name}, admission_number={self.admission_number}, grade_level={self.grade_level}, enrollment_date={self.enrollment_date}>'