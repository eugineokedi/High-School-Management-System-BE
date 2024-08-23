from flask import Blueprint
from flask_restful import Api

# Create a Blueprint for the API
api_bp = Blueprint('api', __name__)
api = Api(api_bp)

# Import route definitions
from .auth_routes import AuthLogin, AuthSignup
from .student_routes import StudentList, StudentDetail
from .teacher_routes import TeacherList, TeacherDetail
from .subject_routes import SubjectList, SubjectDetail
from .grade_routes import GradeList, GradeDetail
from .attendance_routes import AttendanceList, AttendanceDetail
from .event_routes import EventList, EventDetail
from .payment_routes import PaymentList, PaymentDetail
from .book_loan_routes import BookLoanList, BookLoanDetail
from .discipline_record_routes import DisciplineRecordList, DisciplineRecordDetail

# Register routes for authentication
api.add_resource(AuthLogin, '/auth/login')
api.add_resource(AuthSignup, '/auth/signup')

# Register routes for students
api.add_resource(StudentList, '/students')
api.add_resource(StudentDetail, '/students/<int:id>')

# Register routes for teachers
api.add_resource(TeacherList, '/teachers')
api.add_resource(TeacherDetail, '/teachers/<int:id>')

# Register routes for subjects
api.add_resource(SubjectList, '/subjects')
api.add_resource(SubjectDetail, '/subjects/<int:id>')

# Register routes for grades
api.add_resource(GradeList, '/grades')
api.add_resource(GradeDetail, '/grades/<int:student_id>')

# Register routes for attendance
api.add_resource(AttendanceList, '/attendance')
api.add_resource(AttendanceDetail, '/attendance/<int:id>')

# Register routes for events
api.add_resource(EventList, '/events')
api.add_resource(EventDetail, '/events/<int:id>')

# Register routes for payments
api.add_resource(PaymentList, '/payments')
api.add_resource(PaymentDetail, '/payments/<int:id>')

# Register routes for book loans
api.add_resource(BookLoanList, '/book_loans')
api.add_resource(BookLoanDetail, '/book_loans/<int:id>')

# Register routes for discipline records
api.add_resource(DisciplineRecordList, '/discipline_records')
api.add_resource(DisciplineRecordDetail, '/discipline_records/<int:id>')
