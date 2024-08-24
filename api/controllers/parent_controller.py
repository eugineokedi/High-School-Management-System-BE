from flask import Blueprint, jsonify, request
from api.models import db
from models import Parent
from sqlalchemy.exc import IntegrityError

parent_bp = Blueprint('parent', __name__)

# CREATE a new parent
@parent_bp.route('/parents', methods=['POST'])
def create_parent():
    data = request.get_json()
    
    # Check for required fields
    if not data or 'name' not in data or 'contact_number' not in data or 'address' not in data or 'user_id' not in data:
        return jsonify({'error': "Invalid data: 'name', 'contact_number', 'address', and 'user_id' are required fields."}), 400
    
    new_parent = Parent(
        name=data['name'],
        contact_number=data['contact_number'],
        address=data['address'],
        user_id=data['user_id']
    )
    
    try:
        db.session.add(new_parent)
        db.session.commit()
        return jsonify({'message': 'Parent created successfully', 'parent': new_parent.__repr__()}), 201
    except IntegrityError as e:
        db.session.rollback()
        return jsonify({'error': f"Database Integrity Error: {str(e.orig)}"}), 400

# READ all parents
@parent_bp.route('/parents', methods=['GET'])
def get_parents():
    parents = Parent.query.all()
    return jsonify([parent.__repr__() for parent in parents]), 200

# READ a single parent by ID
@parent_bp.route('/parents/<int:id>', methods=['GET'])
def get_parent(id):
    parent = Parent.query.get(id)
    
    if parent is None:
        return jsonify({'error': 'Parent not found'}), 404
    
    return jsonify({'parent': parent.__repr__()}), 200

# UPDATE an existing parent
@parent_bp.route('/parents/<int:id>', methods=['PUT'])
def update_parent(id):
    parent = Parent.query.get(id)
    
    if parent is None:
        return jsonify({'error': 'Parent not found'}), 404
    
    data = request.get_json()
    
    # Check for required fields
    if not data or 'name' not in data or 'contact_number' not in data or 'address' not in data or 'user_id' not in data:
        return jsonify({'error': "Invalid data: 'name', 'contact_number', 'address', and 'user_id' are required fields."}), 400
    
    parent.name = data['name']
    parent.contact_number = data['contact_number']
    parent.address = data['address']
    parent.user_id = data['user_id']

    try:
        db.session.commit()
        return jsonify({'message': 'Parent updated successfully', 'parent': parent.__repr__()}), 200
    except IntegrityError as e:
        db.session.rollback()
        return jsonify({'error': f"Database Integrity Error: {str(e.orig)}"}), 400

# DELETE a parent
@parent_bp.route('/parents/<int:id>', methods=['DELETE'])
def delete_parent(id):
    parent = Parent.query.get(id)
    
    if parent is None:
        return jsonify({'error': 'Parent not found'}), 404
    
    try:
        db.session.delete(parent)
        db.session.commit()
        return jsonify({'message': 'Parent deleted successfully'}), 204
    except IntegrityError as e:
        db.session.rollback()
        return jsonify({'error': f"Database Integrity Error: {str(e.orig)}"}), 400
