# Manages grades and report cards
from flask import Blueprint, request, jsonify
from . import db
from models import Grade, Student, Class
from datetime import datetime, timezone
from sqlalchemy import func

grade_bp = Blueprint('grades', __name__)

@grade_bp.route('/grades', methods=['POST'])
def create_grade():
    data = request.get_json()
    new_grade = Grade(
        score=data['score'],
        assignment_name=data['assignment_name'],
        student_id=data['student_id'],
        class_id=data['class_id'],
        date_submitted=datetime.now(timezone.utc),
        updated_at=datetime.now(timezone.utc)
    )
    
    try:
        db.session.add(new_grade)
        db.session.commit()
        return jsonify({"message": "Grade created successfully", "grade": new_grade.id}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500

@grade_bp.route('/grades/<int:grade_id>', methods=['GET'])
def get_grade(grade_id):
    grade = Grade.query.get(grade_id)
    if not grade:
        return jsonify({"message": "Grade not found"}), 404

    return jsonify({
        "id": grade.id,
        "score": grade.score,
        "date_submitted": grade.date_submitted,
        "updated_at": grade.updated_at,
        "assignment_name": grade.assignment_name,
        "student_id": grade.student_id,
        "class_id": grade.class_id
    }), 200

@grade_bp.route('/grades', methods=['GET'])
def get_all_grades():
    grades = Grade.query.all()
    return jsonify([{
        "id": grade.id,
        "score": grade.score,
        "date_submitted": grade.date_submitted,
        "updated_at": grade.updated_at,
        "assignment_name": grade.assignment_name,
        "student_id": grade.student_id,
        "class_id": grade.class_id
    } for grade in grades]), 200

@grade_bp.route('/grades/<int:grade_id>', methods=['PUT'])
def update_grade(grade_id):
    grade = Grade.query.get(grade_id)
    if not grade:
        return jsonify({"message": "Grade not found"}), 404

    data = request.get_json()
    try:
        grade.score = data.get('score', grade.score)
        grade.assignment_name = data.get('assignment_name', grade.assignment_name)
        grade.updated_at = datetime.now(timezone.utc)
        
        db.session.commit()
        return jsonify({"message": "Grade updated successfully"}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500

@grade_bp.route('/grades/<int:grade_id>', methods=['DELETE'])
def delete_grade(grade_id):
    grade = Grade.query.get(grade_id)
    if not grade:
        return jsonify({"message": "Grade not found"}), 404

    try:
        db.session.delete(grade)
        db.session.commit()
        return jsonify({"message": "Grade deleted successfully"}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500

# Generate Report Card for a Student
@grade_bp.route('/report_card/<int:student_id>', methods=['GET'])
def get_report_card(student_id):
    # Get grades for a student
    grades = Grade.query.filter_by(student_id=student_id).all()

    if not grades:
        return jsonify({"message": "No grades found for this student"}), 404

    # Calculate the average score for all grades as a GPA (or similar metric)
    total_score = sum([grade.score for grade in grades])
    average_score = total_score / len(grades) if len(grades) > 0 else 0

    # Build the report card details
    report_card = {
        "student_id": student_id,
        "grades": [{
            "id": grade.id,
            "assignment_name": grade.assignment_name,
            "score": grade.score,
            "class_id": grade.class_id,
            "date_submitted": grade.date_submitted
        } for grade in grades],
        "total_score": total_score,
        "average_score": round(average_score, 2)
    }

    return jsonify(report_card), 200
