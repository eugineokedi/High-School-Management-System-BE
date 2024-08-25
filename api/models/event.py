from api.models import db
from datetime import datetime
from sqlalchemy_serializer import SerializerMixin

class Event(db.Model, SerializerMixin):
    __tablename__ = 'events'

    id = db.Column(db.Integer, primary_key=True)
    event_name = db.Column(db.String(255), nullable=False)
    event_date = db.Column(db.Date, nullable=False, index=True)
    location = db.Column(db.String(255), nullable=False, index=True)
    description = db.Column(db.String(500), nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)

    # Relationships
    student = db.relationship('Student', back_populates='events', cascade='all, delete-orphan')

    def __repr__(self):
        return f'<Event id={self.id}, event_name={self.event_name}, event_date={self.event_date}, location={self.location}, description={self.description}>'
