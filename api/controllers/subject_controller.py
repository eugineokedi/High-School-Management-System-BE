# Manages subjects (create, update, delete)
from flask import Blueprint, jsonify, request
from models import Subject, db
from sqlalchemy.exc import IntegrityError

subject_bp = Blueprint('subject', __name__)

# CREATE a new subject
@subject_bp.route('/subjects', methods=['POST'])
def create_subject():
    data = request.get_json()
    
    # Check for required fields
    if not data or 'name' not in data or 'description' not in data:
        return jsonify({'error': "Invalid data: 'name' and 'description' are required fields."}), 400
    
    new_subject = Subject(
        name=data['name'],
        description=data['description']
    )
    
    try:
        db.session.add(new_subject)
        db.session.commit()
        return jsonify(new_subject.serialize()), 201
    except IntegrityError as e:
        db.session.rollback()
        return jsonify({'error': f"Database Integrity Error: {str(e.orig)}"}), 400

# READ all subjects
@subject_bp.route('/subjects', methods=['GET'])
def get_subjects():
    subjects = Subject.query.all()
    return jsonify([subject.serialize() for subject in subjects]), 200

# READ a single subject by ID
@subject_bp.route('/subjects/<int:id>', methods=['GET'])
def get_subject(id):
    subject = Subject.query.get(id)
    
    if subject is None:
        return jsonify({'error': 'Subject not found'}), 404
    
    return jsonify(subject.serialize()), 200

# UPDATE an existing subject
@subject_bp.route('/subjects/<int:id>', methods=['PUT'])
def update_subject(id):
    subject = Subject.query.get(id)
    
    if subject is None:
        return jsonify({'error': 'Subject not found'}), 404
    
    data = request.get_json()
    
    # Check for required fields
    if not data or 'name' not in data or 'description' not in data:
        return jsonify({'error': "Invalid data: 'name' and 'description' are required fields."}), 400
    
    subject.name = data['name']
    subject.description = data['description']

    try:
        db.session.commit()
        return jsonify(subject.serialize()), 200
    except IntegrityError as e:
        db.session.rollback()
        return jsonify({'error': f"Database Integrity Error: {str(e.orig)}"}), 400

# DELETE a subject
@subject_bp.route('/subjects/<int:id>', methods=['DELETE'])
def delete_subject(id):
    subject = Subject.query.get(id)
    
    if subject is None:
        return jsonify({'error': 'Subject not found'}), 404
    
    try:
        db.session.delete(subject)
        db.session.commit()
        return jsonify({'message': 'Subject deleted successfully'}), 204
    except IntegrityError as e:
        db.session.rollback()
        return jsonify({'error': f"Database Integrity Error: {str(e.orig)}"}), 400
