from api.models import db
import enum
from datetime import datetime, timezone

class RoleEnum(enum.Enum):
  admin = 'admin'
  teacher = 'teacher'
  student = 'student'
  parent = 'parent'

class User(db.Model):
  __tablename__ = 'users'

  id = db.Column(db.Integer, primary_key=True)
  email = db.Column(db.String, unique=True, nullable=False)
  password_hash = db.Column(db.String, nullable=False)
  created_at = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc), nullable=False)
  role = db.Column(db.Enum(RoleEnum), nullable=False)

  # Relationships
  parent = db.relationship('Parent', back_populates='user', useList=False)
  teacher = db.relationship('Teacher', back_populates='user', useList=False)
  student = db.relationship('Student', back_populates='user', useList=False)

  def __repr__(self):
      return f'<User id={self.id}, email={self.email}, datetime={self.created_at}, role={self.role.value}>'