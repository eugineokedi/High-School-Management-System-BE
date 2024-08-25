from api.models import db
from datetime import datetime, timezone
from sqlalchemy_serializer import SerializerMixin

class Grade(db.Model, SerializerMixin):
    __tablename__ = 'grades'

    id = db.Column(db.Integer, primary_key=True)
    score = db.Column(db.Integer, nullable=False)
    date_submitted = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc), nullable=False)
    updated_at = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc), onupdate=lambda: datetime.now(timezone.utc), nullable=False)
    assignment_name = db.Column(db.String(255), nullable=False)
    student_id = db.Column(db.Integer, db.ForeignKey('students.id'), nullable=False, index=True)
    class_id = db.Column(db.Integer, db.ForeignKey('classes.id'), nullable=False, index=True)

    # Relationships
    student = db.relationship('Student', back_populates='grades')
    class_ = db.relationship('Class', back_populates='grades')

    def __repr__(self):
        return f'<Grade id={self.id}, score={self.score}, date_submitted={self.date_submitted}, updated_at={self.updated_at}, assignment_name={self.assignment_name}>'
