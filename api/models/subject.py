from api.models import db

class Subject(db.Model):
  __tablename__ = 'subjects'

  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(100), nullable=False)
  description = db.Column(db.String(255), nullable=False)

  def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description
        }
  
  def __repr__(self):
    return f'<Subject id={self.id}, name={self.name}, description={self.description}>'