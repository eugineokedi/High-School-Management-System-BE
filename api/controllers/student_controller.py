# Handles CRUD operations for students
from flask import Blueprint, request, jsonify
from api.models import db
from models import Student
from datetime import datetime

student_bp = Blueprint('student_bp', __name__)

# Retrieve all students
@student_bp.route('/students', methods=['GET'])
def get_students():
    students = Student.query.all()
    return jsonify([student.serialize() for student in students]), 200

# Retrieve a single student by ID
@student_bp.route('/students/<int:id>', methods=['GET'])
def get_student(id):
    student = Student.query.get_or_404(id)
    return jsonify(student.serialize()), 200

# Create a new student
@student_bp.route('/students', methods=['POST'])
def create_student():
    data = request.get_json()
    
    try:
        new_student = Student(
            first_name=data['first_name'],
            last_name=data['last_name'],
            admission_number=data['admission_number'],
            date_of_birth=datetime.strptime(data['date_of_birth'], '%Y-%m-%d').date(),
            gender=data['gender'],
            grade_level=data['grade_level'],
            user_id=data['user_id']
        )
        
        db.session.add(new_student)
        db.session.commit()
        
        return jsonify(new_student.serialize()), 201
    
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 400

# Update a student by ID
@student_bp.route('/students/<int:id>', methods=['PUT'])
def update_student(id):
    student = Student.query.get_or_404(id)
    data = request.get_json()

    student.first_name = data.get('first_name', student.first_name)
    student.last_name = data.get('last_name', student.last_name)
    student.admission_number = data.get('admission_number', student.admission_number)
    student.date_of_birth = datetime.strptime(data.get('date_of_birth', student.date_of_birth.strftime('%Y-%m-%d')), '%Y-%m-%d').date()
    student.gender = data.get('gender', student.gender)
    student.grade_level = data.get('grade_level', student.grade_level)
    student.user_id = data.get('user_id', student.user_id)

    db.session.commit()
    
    return jsonify(student.serialize()), 200

# Delete a student by ID
@student_bp.route('/students/<int:id>', methods=['DELETE'])
def delete_student(id):
    student = Student.query.get_or_404(id)
    db.session.delete(student)
    db.session.commit()
    
    return jsonify({"message": "Student deleted successfully"}), 200
