from . import db
import enum

class ActionEnum(enum.Enum):
    Suspended = 'Suspended'
    Expelled = 'Expelled'
    Punished = 'Punished'

class DisciplineRecord(db.Model):
    __tablename__ = 'discipline_records'

    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date, nullable=False)
    infraction = db.Column(db.String(255), nullable=False)
    action_taken = db.Column(db.Enum(ActionEnum), nullable=False) 
    student_id = db.Column(db.Integer, db.ForeignKey('students.id'), nullable=False)

    def __repr__(self):
        return f'<DisciplineRecord id={self.id}, date={self.date}, infraction={self.infraction}, action_taken={self.action_taken.value}>'
