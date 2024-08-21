from . import db

class Parent(db.Model):
  __tablename__ = 'parents'

  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(255), nullable=False)
  contact_number = db.Column(db.String(20), nullable=False)
  address = db.Column(db.String(255), nullable=False)
  user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

  def __repr__(self):
    return f'<Parent id={self.id}, name={self.name}, contact_number={self.contact_number}, address={self.address}>'