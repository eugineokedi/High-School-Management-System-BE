from api.models import db
from sqlalchemy_serializer import SerializerMixin


class ClassSchedule(db.Model, SerializerMixin):
    __tablename__ = 'class_schedules'

    id = db.Column(db.Integer, primary_key=True)
    day_of_week = db.Column(db.String(10), nullable=False)  # e.g., 'Monday', 'Tuesday'
    start_time = db.Column(db.Time, nullable=False)
    end_time = db.Column(db.Time, nullable=False)
    class_id = db.Column(db.Integer, db.ForeignKey('classes.id'), nullable=False)

    # Relationships
    classes = db.relationship('Class', back_populates='class_schedules')

    def __repr__(self):
        return f'<ClassSchedule id={self.id}, day_of_week={self.day_of_week}, start_time={self.start_time}, end_time={self.end_time}>'