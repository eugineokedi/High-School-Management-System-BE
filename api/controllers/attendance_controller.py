# Handles attendance management
from flask import Blueprint, request, jsonify
from api.models import db
from models import Attendance, StatusEnum
from datetime import datetime

attendance_bp = Blueprint('attendance', __name__)

@attendance_bp.route('/attendance', methods=['POST'])
def record_attendance():
    data = request.get_json()

    # Validate input data
    if not all(key in data for key in ('date', 'status', 'student_id', 'class_id')):
        return jsonify({"error": "Missing required fields"}), 400

    try:
        new_attendance = Attendance(
            date=datetime.strptime(data['date'], '%Y-%m-%d').date(),
            status=StatusEnum[data['status']],
            student_id=data['student_id'],
            class_id=data['class_id']
        )
        
        db.session.add(new_attendance)
        db.session.commit()

        return jsonify({"message": "Attendance recorded successfully", "attendance_id": new_attendance.id}), 201

    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500

@attendance_bp.route('/attendance/<int:attendance_id>', methods=['GET'])
def get_attendance(attendance_id):
    attendance = Attendance.query.get(attendance_id)
    if not attendance:
        return jsonify({"message": "Attendance record not found"}), 404

    return jsonify({
        "id": attendance.id,
        "date": attendance.date,
        "status": attendance.status.value,
        "student_id": attendance.student_id,
        "class_id": attendance.class_id
    }), 200

@attendance_bp.route('/attendance', methods=['GET'])
def get_all_attendance():
    attendance_records = Attendance.query.all()
    return jsonify([{
        "id": attendance.id,
        "date": attendance.date,
        "status": attendance.status.value,
        "student_id": attendance.student_id,
        "class_id": attendance.class_id
    } for attendance in attendance_records]), 200

@attendance_bp.route('/attendance/<int:attendance_id>', methods=['PUT'])
def update_attendance(attendance_id):
    attendance = Attendance.query.get(attendance_id)
    if not attendance:
        return jsonify({"message": "Attendance record not found"}), 404

    data = request.get_json()

    try:
        if 'date' in data:
            attendance.date = datetime.strptime(data['date'], '%Y-%m-%d').date()
        if 'status' in data:
            attendance.status = StatusEnum[data['status']]

        db.session.commit()
        return jsonify({"message": "Attendance updated successfully"}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500

@attendance_bp.route('/attendance/<int:attendance_id>', methods=['DELETE'])
def delete_attendance(attendance_id):
    attendance = Attendance.query.get(attendance_id)
    if not attendance:
        return jsonify({"message": "Attendance record not found"}), 404

    try:
        db.session.delete(attendance)
        db.session.commit()
        return jsonify({"message": "Attendance record deleted successfully"}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500
