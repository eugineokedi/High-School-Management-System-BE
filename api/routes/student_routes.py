from flask_restful import Resource
from controllers.student_controller import StudentController

class StudentList(Resource):
    def get(self):
        return StudentController.get_all_students()

    def post(self):
        return StudentController.create_student()

class StudentDetail(Resource):
    def get(self, id):
        return StudentController.get_student(id)

    def put(self, id):
        return StudentController.update_student(id)

    def delete(self, id):
        return StudentController.delete_student(id)
