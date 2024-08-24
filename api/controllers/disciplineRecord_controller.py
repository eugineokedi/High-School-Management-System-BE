from flask import Blueprint, request, jsonify, abort
from api.models import db
from models.disciplineRecord import DisciplineRecord, ActionEnum
from datetime import datetime

# Define a blueprint for discipline record-related routes
discipline_record_bp = Blueprint('discipline_records', __name__)

# Create a new discipline record
@discipline_record_bp.route('/discipline_records', methods=['POST'])
def create_discipline_record():
    data = request.get_json()

    # Validate required fields
    if not all(field in data for field in ['date', 'infraction', 'action_taken', 'student_id']):
        return jsonify({'error': 'Missing required fields'}), 400

    # Validate and parse the date
    try:
        date = datetime.strptime(data['date'], '%Y-%m-%d').date()
    except ValueError:
        return jsonify({'error': 'Invalid date format, expected YYYY-MM-DD'}), 400

    # Validate the action taken
    try:
        action_taken = ActionEnum(data['action_taken'])
    except ValueError:
        return jsonify({'error': 'Invalid action value'}), 400

    # Create the discipline record
    new_record = DisciplineRecord(
        date=date,
        infraction=data['infraction'],
        action_taken=action_taken,
        student_id=data['student_id']
    )

    db.session.add(new_record)
    db.session.commit()

    return jsonify({'message': 'Discipline record created successfully', 'record_id': new_record.id}), 201

# Get a discipline record by ID
@discipline_record_bp.route('/discipline_records/<int:record_id>', methods=['GET'])
def get_discipline_record(record_id):
    record = DisciplineRecord.query.get(record_id)
    if record is None:
        return abort(404, description="Discipline record not found")

    record_data = {
        'id': record.id,
        'date': record.date.strftime('%Y-%m-%d'),
        'infraction': record.infraction,
        'action_taken': record.action_taken.value,
        'student_id': record.student_id
    }

    return jsonify(record_data), 200

# Get all discipline records
@discipline_record_bp.route('/discipline_records', methods=['GET'])
def get_discipline_records():
    records = DisciplineRecord.query.all()
    records_list = [{
        'id': record.id,
        'date': record.date.strftime('%Y-%m-%d'),
        'infraction': record.infraction,
        'action_taken': record.action_taken.value,
        'student_id': record.student_id
    } for record in records]

    return jsonify(records_list), 200

# Update a discipline record
@discipline_record_bp.route('/discipline_records/<int:record_id>', methods=['PUT'])
def update_discipline_record(record_id):
    record = DisciplineRecord.query.get(record_id)
    if record is None:
        return abort(404, description="Discipline record not found")

    data = request.get_json()

    # Update fields if provided
    if 'date' in data:
        try:
            record.date = datetime.strptime(data['date'], '%Y-%m-%d').date()
        except ValueError:
            return jsonify({'error': 'Invalid date format, expected YYYY-MM-DD'}), 400

    if 'infraction' in data:
        record.infraction = data['infraction']
    
    if 'action_taken' in data:
        try:
            record.action_taken = ActionEnum(data['action_taken'])
        except ValueError:
            return jsonify({'error': 'Invalid action value'}), 400

    db.session.commit()

    return jsonify({'message': 'Discipline record updated successfully'}), 200

# Delete a discipline record
@discipline_record_bp.route('/discipline_records/<int:record_id>', methods=['DELETE'])
def delete_discipline_record(record_id):
    record = DisciplineRecord.query.get(record_id)
    if record is None:
        return abort(404, description="Discipline record not found")

    db.session.delete(record)
    db.session.commit()

    return jsonify({'message': 'Discipline record deleted successfully'}), 200
