from . import db

class Class(db.Model):
  __tablename__ = 'classes'

  id = db.Column(db.Integer, primary_key=True)
  class_name = db.Column(db.String(100), nullable=False)
  subject = db.Column(db.String(100), nullable=False)
  schedule = db.Column(db.String(255), nullable=False)

  def __repr__(self):
    return f'<Class id={self.id}, class_name={self.class_name}, subject={self.subject}, schedule={self.schedule}>'