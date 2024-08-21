# Handles CRUD operations for teachers
from flask import Blueprint, request, jsonify
from models import Teacher, db
from datetime import datetime
from sqlalchemy.exc import IntegrityError

teacher_bp = Blueprint('teacher_bp', __name__)

# Route to fetch all teachers
@teacher_bp.route('/teachers', methods=['GET'])
def get_teachers():
    teachers = Teacher.query.all()
    return jsonify([teacher.serialize() for teacher in teachers]), 200

# Route to fetch a single teacher by ID
@teacher_bp.route('/teachers/<int:id>', methods=['GET'])
def get_teacher(id):
    teacher = Teacher.query.get_or_404(id)
    return jsonify(teacher.serialize()), 200

# Route to add a new teacher
@teacher_bp.route('/teachers', methods=['POST'])
def create_teacher():
    try:
        data = request.get_json()
        
        new_teacher = Teacher(
            name=data['name'],
            subject=data['subject'],
            hire_date=datetime.utcnow(),
            qualification=data['qualification'],
            user_id=data['user_id']
        )
        
        db.session.add(new_teacher)
        db.session.commit()
        
        return jsonify(new_teacher.serialize()), 201
    
    except IntegrityError:
        db.session.rollback()
        return jsonify({"error": "User ID already exists or other integrity error"}), 400
    except KeyError:
        return jsonify({"error": "Missing required data"}), 400

# Route to update a teacher's details
@teacher_bp.route('/teachers/<int:id>', methods=['PUT'])
def update_teacher(id):
    teacher = Teacher.query.get_or_404(id)
    data = request.get_json()

    teacher.name = data.get('name', teacher.name)
    teacher.subject = data.get('subject', teacher.subject)
    teacher.hire_date = datetime.strptime(data.get('hire_date', teacher.hire_date.strftime('%Y-%m-%d')), '%Y-%m-%d') if 'hire_date' in data else teacher.hire_date
    teacher.qualification = data.get('qualification', teacher.qualification)
    teacher.user_id = data.get('user_id', teacher.user_id)

    db.session.commit()
    
    return jsonify(teacher.serialize()), 200

# Route to delete a teacher
@teacher_bp.route('/teachers/<int:id>', methods=['DELETE'])
def delete_teacher(id):
    teacher = Teacher.query.get_or_404(id)
    db.session.delete(teacher)
    db.session.commit()
    
    return jsonify({"message": "Teacher deleted successfully"}), 200
