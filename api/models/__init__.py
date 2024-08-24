from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# Import models to be accessible
from .user import User
from .student import Student
from .teacher import Teacher
from .subject import Subject
from .grade import Grade
from .attendance import Attendance
from .parent import Parent
from .school_class import Class
from .bookLoan import BookLoan
from .libraryBook import LibraryBook
from .event import Event
from .enrollment import Enrollment
from .payment import Payment
from .disciplineRecord import DisciplineRecord
from .classSchedule import ClassSchedule
