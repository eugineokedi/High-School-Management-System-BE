from api.models import db
from sqlalchemy_serializer import SerializerMixin

class Parent(db.Model, SerializerMixin):
  __tablename__ = 'parents'

  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(255), nullable=False)
  occupation = db.Column(db.String(100), nullable=False)
  contact_number = db.Column(db.String(20), nullable=False)
  address = db.Column(db.String(255), nullable=False)
  user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
  
  # Relationships
  students = db.relationship('Student', back_populates='parent', cascade='all, delete-orphan')
  user = db.relationship('User', back_populates='parent', uselist=False)

  def __repr__(self):
    return f'<Parent id={self.id}, name={self.name}, contact_number={self.contact_number}, address={self.address}>'