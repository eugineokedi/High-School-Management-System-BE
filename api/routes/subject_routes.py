from flask_restful import Resource
from controllers.subject_controller import SubjectController

class SubjectList(Resource):
    def get(self):
        return SubjectController.get_all_courses()

    def post(self):
        return SubjectController.create_course()

class SubjectDetail(Resource):
    def get(self, id):
        return SubjectController.get_course(id)

    def put(self, id):
        return SubjectController.update_course(id)

    def delete(self, id):
        return SubjectController.delete_course(id)
