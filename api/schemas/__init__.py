from marshmallow import Schema, fields, validate

# Import the individual schemas
from .user_schema import UserSchema
from .student_schema import StudentSchema
from .teacher_schema import TeacherSchema
from .subject_schema import SubjectSchema
from .grade_schema import GradeSchema
from .attendance_schema import AttendanceSchema
