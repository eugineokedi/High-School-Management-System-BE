from config import db, app
from api.models import User, Teacher, Student, Parent, Class, Subject, Payment, LibraryBook, DisciplineRecord, Enrollment, Event, BookLoan, Attendance, Grade
from sqlalchemy.exc import IntegrityError

def seed_data():
  with app.app_context():
    # Clear existing data
    db.session.query(User).delete()
    db.session.query(Teacher).delete()
    db.session.query(Student).delete()
    db.session.query(Parent).delete()
    db.session.query(Class).delete()
    db.session.query(Subject).delete()
    db.session.query(Payment).delete()
    db.session.query(LibraryBook).delete()
    db.session.query(DisciplineRecord).delete()
    db.session.query(Enrollment).delete()
    db.session.query(Event).delete()
    db.session.query(BookLoan).delete()
    db.session.query(Attendance).delete()
    db.session.query(Grade).delete()
    db.session.query(Attendance).delete()

    # Add Users
    users = [
      User(email='admin@example.com', password_hash='password123', role='admin'),
      User(email='teacher@example.com', password_hash='password123', role='teacher'),
      User(email='student@example.com', password_hash='password123', role='student'),
      User(email='parent@example.com', password_hash='password123', role='parent')
    ]





    try:
      # Commit all changes
      db.session.commit()
      print("Database seeded with new data!")
    except IntegrityError:
      db.session.rollback()
      print("Integrity error occurred. Database rollback.")

if __name__ == "__main__":
    seed_data()
