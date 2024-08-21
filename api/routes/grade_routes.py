from flask_restful import Resource
from controllers.grade_controller import GradeController

class GradeList(Resource):
    def get(self):
        return GradeController.get_all_grades()

    def post(self):
        return GradeController.create_grade()

class GradeDetail(Resource):
    def get(self, student_id):
        return GradeController.get_grades_by_student(student_id)
