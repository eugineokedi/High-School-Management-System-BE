from flask_restful import Resource
from controllers.attendance_controller import AttendanceController

class AttendanceList(Resource):
    def get(self):
        return AttendanceController.get_all_attendance()

    def post(self):
        return AttendanceController.record_attendance()

class AttendanceDetail(Resource):
    def get(self, id):
        return AttendanceController.get_attendance(id)

    def put(self, id):
        return AttendanceController.update_attendance(id)
