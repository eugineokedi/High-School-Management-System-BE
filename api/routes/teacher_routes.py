from flask_restful import Resource
from controllers.teacher_controller import TeacherController

class TeacherList(Resource):
    def get(self):
        return TeacherController.get_all_teachers()

    def post(self):
        return TeacherController.create_teacher()

class TeacherDetail(Resource):
    def get(self, id):
        return TeacherController.get_teacher(id)

    def put(self, id):
        return TeacherController.update_teacher(id)

    def delete(self, id):
        return TeacherController.delete_teacher(id)
