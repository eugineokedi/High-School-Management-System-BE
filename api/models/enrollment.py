from . import db

class Enrollment(db.Model):
    __tablename__ = 'enrollments'

    id = db.Column(db.Integer, primary_key=True)
    enrollment_date = db.Column(db.Date, nullable=False)
    grade = db.Column(db.String(10), nullable=False)
    class_id = db.Column(db.Integer, db.ForeignKey('classes.id'), nullable=False)
    student_id = db.Column(db.Integer, db.ForeignKey('students.id'), nullable=False)

    def __repr__(self):
        return f'<Enrollment id={self.id}, enrollment_date={self.enrollment_date}, grade={self.grade}>'
