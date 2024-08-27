from app import app, bcrypt
from api.models import User, Teacher, Student, Parent, Class, Subject, Payment, LibraryBook, DisciplineRecord, Enrollment, Event, BookLoan, Attendance, Grade, db
from sqlalchemy.exc import IntegrityError
from api.models.disciplineRecord import ActionEnum
from api.models.enrollment import GradeEnum
from api.models.bookLoan import BookLoanEnum
from api.models.attendance import StatusEnum
from api.models.libraryBook import AvailabilityEnum
from api.models.payment import PaymentStatusEnum, PaymentMethodEnum
from api.models.user import RoleEnum
from datetime import datetime, timezone

def hash_password(password):
    return bcrypt.generate_password_hash(password).decode('utf-8')

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

    # Add Users
    users = [
      User(email='cyrusmatheri@gmail.com', password_hash=hash_password('password@123'), role=RoleEnum.teacher),
      User(email='lukoritoalexx@gmail.com', password_hash=hash_password('password@123'), role=RoleEnum.teacher),
      User(email='clintonkibet@gmail.com', password_hash=hash_password('password@123'), role=RoleEnum.teacher),
      User(email='edwardmwangi@gmail.com', password_hash=hash_password('password@123'), role=RoleEnum.teacher),
      User(email='josephwilliams@gmail.com', password_hash=hash_password('password@123'), role=RoleEnum.parent),
      User(email='sarahkim@gmail.com', password_hash=hash_password('password@123'), role=RoleEnum.parent),
      User(email='davidkim@gmail.com', password_hash=hash_password('password@123'), role=RoleEnum.parent),
      User(email='danielkim@gmail.com', password_hash=hash_password('password@123'), role=RoleEnum.student),
      User(email='julietkim@gmail.com', password_hash=hash_password('password@123'), role=RoleEnum.student),
      User(email='georgekim@gmail.com', password_hash=hash_password('password@123'), role=RoleEnum.student),
      User(email='johnnykim@gmail.com', password_hash=hash_password('password@123'), role=RoleEnum.student),
      User(email='marykim@gmail.com', password_hash=hash_password('password@123'), role=RoleEnum.student),
      User(email='michaelkim@gmail.com', password_hash=hash_password('password@123'), role=RoleEnum.student),
      User(email='kevinkim@gmail.com', password_hash=hash_password('password@123'), role=RoleEnum.student)
    ]
    db.session.add_all(users)

    # Add Teachers
    teachers = [
      Teacher(name='Mr. Matheri', subject='Mathematics', qualification='BSc', user_id=1),
      Teacher(name='Mr. Alex', subject='Biology', qualification='MBA', user_id=2),
      Teacher(name='Mr. Clinton', subject='English', qualification='PhD', user_id=3),
      Teacher(name='Ms. Mwangi', subject='History', qualification='MBA', user_id=4)
    ]
    db.session.add_all(teachers)

    # Add Students
    students = [
      Student(first_name='Dabiel', last_name='Kim', admission_number='855', date_of_birth=datetime(2000, 1, 1), gender='Male', grade_level=12, user_id=8, parent_id=1, event_id=1),
      Student(first_name='Juliet', last_name='Kim', admission_number='856', date_of_birth=datetime(2001, 1, 1), gender='Female', grade_level=11, user_id=9, parent_id=1, event_id=3),
      Student(first_name='George', last_name='Kim', admission_number='857', date_of_birth=datetime(2002, 1, 1), gender='Male', grade_level=10, user_id=10, parent_id=2, event_id=2),
      Student(first_name='johnny', last_name='Kim', admission_number='858', date_of_birth=datetime(2003, 1, 1), gender='Male', grade_level=9, user_id=11, parent_id=2, event_id=1),
      Student(first_name='Mary', last_name='Kim', admission_number='859', date_of_birth=datetime(2004, 1, 1), gender='Female', grade_level=8, user_id=12, parent_id=3, event_id=3),
      Student(first_name='Michael', last_name='Kim', admission_number='860', date_of_birth=datetime(2005, 1, 1), gender='Male', grade_level=7, user_id=13,  parent_id=3, event_id=2),
      Student(first_name='Kevin', last_name='Kim', admission_number='861', date_of_birth=datetime(2006, 1, 1), gender='Male', grade_level=6, user_id=14, parent_id=3, event_id=1)
    ]
    db.session.add_all(students)

    # Add Parents
    parents = [
      Parent(name='Joseph Williams', occupation='Doctor',  contact_number='080-123-4567', address='123 Main St', user_id=5),
      Parent(name='Sarah Kim', occupation='Teacher', contact_number='090-987-6543', address='123 Main St', user_id=6),
      Parent(name='David Kim', occupation='Engineer', contact_number='070-555-5555', address='123 Main St', user_id=7)
    ]
    db.session.add_all(parents)

    # Add Classes
    classes = [
        Class(class_name='Form 1W', teacher_id=1),
        Class(class_name='Form 2X', teacher_id=2),
        Class(class_name='Form 3Y', teacher_id=3),
        Class(class_name='Form 4Z', teacher_id=4)
    ]
    db.session.add_all(classes)

    # Add Subjects
    subjects = [
        Subject(subject_name='Mathematics', description='An exploration of numbers, equations, and problem-solving techniques.', class_id=1),
        Subject(subject_name='Biology', description='Study of living organisms, including their structure, function, and growth.', class_id=2),
        Subject(subject_name='English', description='Focus on reading, writing, and literature analysis, enhancing communication skills.', class_id=3),
        Subject(subject_name='History', description='A survey of past events and civilizations, and their impact on the modern world.', class_id=4)
    ] 
    db.session.add_all(subjects)

    # Add Payments
    payments = [
        Payment(amount=30000.00, amount_due=24000.00, payment_date=datetime(2022, 1, 1), payment_method=PaymentMethodEnum.M_pesa, status=PaymentStatusEnum.Paid, student_id=8),
        Payment(amount=11500.00, amount_due=42500.00, payment_date=datetime(2022, 2, 1), payment_method=PaymentMethodEnum.Credit_card, status=PaymentStatusEnum.Paid, student_id=9),
        Payment(amount=22000.00, amount_due=34000.00, payment_date=datetime(2022, 3, 1), payment_method=PaymentMethodEnum.Bank_transfer, status=PaymentStatusEnum.Paid, student_id=10),
        Payment(amount=35000.00, amount_due=19000.00, payment_date=datetime(2022, 4, 1), payment_method=PaymentMethodEnum.Bank_transfer, status=PaymentStatusEnum.Paid, student_id=11),
        Payment(amount=0.00, amount_due=54000.00, payment_date=datetime(2022, 5, 1), payment_method=PaymentMethodEnum.Credit_card, status=PaymentStatusEnum.Not_paid, student_id=12),
        Payment(amount=45700.00, amount_due=8300.00, payment_date=datetime(2022, 6, 1), payment_method=PaymentMethodEnum.M_pesa, status=PaymentStatusEnum.Paid, student_id=13),
        Payment(amount=38000.00, amount_due=16000.00, payment_date=datetime(2023, 4, 1), payment_method=PaymentMethodEnum.M_pesa, status=PaymentStatusEnum.Paid, student_id= 14)
    ]
    db.session.add_all(payments)

    # Add LibraryBook
    library_books = [
       LibraryBook(title='Mathematics Book 1', author='Kenya Literature Bureau', isbn='9780060935467', availability=AvailabilityEnum.Available),
       LibraryBook(title='English Book 2', author='Kenya Literature Bureau', isbn='9780060935468', availability=AvailabilityEnum.Available),
       LibraryBook(title='History Book 3', author='Kenya Literature Bureau', isbn='9780060935469', availability=AvailabilityEnum.Checked_out),
       LibraryBook(title='Geography Book 4', author='Kenya Literature Bureau', isbn='9780060935470', availability=AvailabilityEnum.Checked_out),
       LibraryBook(title='Kiswahili Book 3', author='Kenya Literature Bureau', isbn='9780060935471', availability=AvailabilityEnum.Available),
       LibraryBook(title='The River and The Source', author='Margaret Ogola', isbn='9780060935472', availability=AvailabilityEnum.Reserved),
       LibraryBook(title='Damu Nyeusi', author='Ken Walibora', isbn='9780060935473', availability=AvailabilityEnum.Reserved)
    ]
    db.session.add_all(library_books)

    # Add DisciplineRecord
    discipline_records = [
        DisciplineRecord(date=datetime(2024, 1, 15), infraction='Fighting with another student', action_taken=ActionEnum.Suspended, student_id=1),
        DisciplineRecord(date=datetime(2024, 2, 10), infraction='Cheating on an exam', action_taken=ActionEnum.Punished, student_id=2),
        DisciplineRecord(date=datetime(2024, 3, 5), infraction='Vandalism of school property', action_taken=ActionEnum.Suspended, student_id=3),
        DisciplineRecord(date=datetime(2024, 4, 20), infraction='Bullying', action_taken=ActionEnum.Expelled, student_id=4),
        DisciplineRecord(date=datetime(2024, 5, 25), infraction='Using inappropriate language towards a teacher', action_taken=ActionEnum.Punished, student_id=5),
        DisciplineRecord(date=datetime(2024, 6, 15), infraction='Skipping classes repeatedly', action_taken=ActionEnum.Suspended, student_id=6),
        DisciplineRecord(date=datetime(2024, 7, 1), infraction='Theft of school materials', action_taken=ActionEnum.Expelled, student_id=7)
    ]
    db.session.add_all(discipline_records)

    # Add Enrollment
    enrollments = [
        Enrollment(enrollment_date=datetime(2023, 9, 1), grade=GradeEnum.A, class_id=1, student_id=1),
        Enrollment(enrollment_date=datetime(2023, 9, 1), grade=GradeEnum.B_plus, class_id=2, student_id=2),
        Enrollment(enrollment_date=datetime(2023, 9, 1), grade=GradeEnum.C, class_id=3, student_id=3),
        Enrollment(enrollment_date=datetime(2023, 9, 1), grade=GradeEnum.A_minus, class_id=3, student_id=4),
        Enrollment(enrollment_date=datetime(2023, 9, 1), grade=GradeEnum.B_minus, class_id=2, student_id=5),
        Enrollment(enrollment_date=datetime(2023, 9, 1), grade=GradeEnum.C_plus, class_id=1, student_id=6),
        Enrollment(enrollment_date=datetime(2023, 9, 1), grade=GradeEnum.D, class_id=3, student_id=7)
    ]
    db.session.add_all(enrollments)

    # Add Events
    events = [
        Event(event_name='Science Fair', event_date=datetime(2024, 5, 15), location='Auditorium', description='Annual science fair showcasing student projects.'),
        Event(event_name='Sports Day', event_date=datetime(2024, 6, 20), location='Sports Complex', description='Inter-school sports competition.'),
        Event(event_name='Art Exhibition', event_date=datetime(2024, 7, 10), location='Art Gallery', description='Exhibition of student artwork.'),
        Event(event_name='Music Concert', event_date=datetime(2024, 8, 25), location='Main Hall', description='End of year concert featuring student performances.'),
        Event(event_name='Graduation Ceremony', event_date=datetime(2024, 9, 5), location='School Grounds', description='Graduation ceremony for the senior class.'),
        Event(event_name='Debate Competition', event_date=datetime(2024, 10, 12), location='Conference Room', description='Debate competition between students.'),
        Event(event_name='School Play', event_date=datetime(2024, 11, 18), location='Theatre', description='Performance of the annual school play.')
    ]
    db.session.add_all(events)

    # Add BookLoan
    book_loans = [
        BookLoan(borrow_date=datetime(2024, 1, 10), return_date=datetime(2024, 1, 25), status=BookLoanEnum.returned, student_id=1, book_id=1),
        BookLoan(borrow_date=datetime(2024, 2, 5), return_date=datetime(2024, 2, 20), status=BookLoanEnum.returned, student_id=2, book_id=2),
        BookLoan(borrow_date=datetime(2024, 3, 15), return_date=None, status=BookLoanEnum.borrowed, student_id=3, book_id=3),
        BookLoan(borrow_date=datetime(2024, 4, 1), return_date=datetime(2024, 4, 15), status=BookLoanEnum.returned, student_id=4, book_id=4),
        BookLoan(borrow_date=datetime(2024, 5, 10), return_date=None, status=BookLoanEnum.overdue, student_id=5, book_id=5),
        BookLoan(borrow_date=datetime(2024, 6, 20), return_date=None, status=BookLoanEnum.borrowed, student_id=6, book_id=6),
        BookLoan(borrow_date=datetime(2024, 7, 25), return_date=None, status=BookLoanEnum.overdue, student_id=7, book_id=7)
    ]
    db.session.add_all(book_loans)

    # Add Attendance
    attendances = [
        Attendance(date=datetime(2024, 1, 10), status=StatusEnum.present, student_id=1, class_id=1),
        Attendance(date=datetime(2024, 1, 11), status=StatusEnum.absent, student_id=2, class_id=1),
        Attendance(date=datetime(2024, 1, 12), status=StatusEnum.late, student_id=3, class_id=2),
        Attendance(date=datetime(2024, 1, 13), status=StatusEnum.present, student_id=4, class_id=2),
        Attendance(date=datetime(2024, 1, 14), status=StatusEnum.absent, student_id=5, class_id=3),
        Attendance(date=datetime(2024, 1, 15), status=StatusEnum.late, student_id=6, class_id=3),
        Attendance(date=datetime(2024, 1, 16), status=StatusEnum.present, student_id=7, class_id=4)
    ]
    db.session.add_all(attendances)

    # Add Grade
    grades = [
        Grade(score=85, date_submitted=datetime(2024, 1, 10, tzinfo=timezone.utc), assignment_name='Math Assignment 1', student_id=1, class_id=1),
        Grade(score=90, date_submitted=datetime(2024, 1, 12, tzinfo=timezone.utc), assignment_name='Science Project', student_id=2, class_id=2),
        Grade(score=75, date_submitted=datetime(2024, 1, 14, tzinfo=timezone.utc), assignment_name='History Essay', student_id=3, class_id=3),
        Grade(score=88, date_submitted=datetime(2024, 1, 16, tzinfo=timezone.utc), assignment_name='English Paper', student_id=4, class_id=4),
        Grade(score=92, date_submitted=datetime(2024, 1, 18, tzinfo=timezone.utc), assignment_name='Art Project', student_id=5, class_id=5),
        Grade(score=80, date_submitted=datetime(2024, 1, 20, tzinfo=timezone.utc), assignment_name='Physics Lab Report', student_id=6, class_id=6),
        Grade(score=95, date_submitted=datetime(2024, 1, 22, tzinfo=timezone.utc), assignment_name='Chemistry Experiment', student_id=7, class_id=7)
    ]
    db.session.add_all(grades)

    try:
      # Commit all changes
      db.session.commit()
      print("Database seeded with new data!")
    except IntegrityError:
      db.session.rollback()
      print("Integrity error occurred. Database rollback.")

if __name__ == "__main__":
    seed_data()
