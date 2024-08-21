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

# Register routes
api.add_resource(AuthLogin, '/auth/login')
api.add_resource(AuthSignup, '/auth/signup')
api.add_resource(StudentList, '/students')
api.add_resource(StudentDetail, '/students/<int:id>')
api.add_resource(TeacherList, '/teachers')
api.add_resource(TeacherDetail, '/teachers/<int:id>')
api.add_resource(SubjectList, '/subjects')
api.add_resource(SubjectDetail, '/subjects/<int:id>')
api.add_resource(GradeList, '/grades')
api.add_resource(GradeDetail, '/grades/<int:student_id>')
api.add_resource(AttendanceList, '/attendance')
api.add_resource(AttendanceDetail, '/attendance/<int:id>')
