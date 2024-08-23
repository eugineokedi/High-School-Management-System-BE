from flask import Blueprint, request, jsonify, abort
from . import db
from api.models.event import Event
from datetime import datetime

# Define a blueprint for event-related routes
event_bp = Blueprint('events', __name__)

# Create a new event
@event_bp.route('/events', methods=['POST'])
def create_event():
    data = request.get_json()
    
    # Validate required fields
    if not all(field in data for field in ['event_name', 'event_date', 'location']):
        return jsonify({'error': 'Missing required fields'}), 400
    
    try:
        event_date = datetime.strptime(data['event_date'], '%Y-%m-%d').date()
    except ValueError:
        return jsonify({'error': 'Invalid date format, expected YYYY-MM-DD'}), 400

    # Create the event
    new_event = Event(
        event_name=data['event_name'],
        event_date=event_date,
        location=data['location'],
        description=data.get('description', '')  # Optional field
    )
    
    db.session.add(new_event)
    db.session.commit()

    return jsonify({'message': 'Event created successfully', 'event': new_event.id}), 201

# Get an event by ID
@event_bp.route('/events/<int:event_id>', methods=['GET'])
def get_event(event_id):
    event = Event.query.get(event_id)
    if event is None:
        return abort(404, description="Event not found")

    event_data = {
        'id': event.id,
        'event_name': event.event_name,
        'event_date': event.event_date.strftime('%Y-%m-%d'),
        'location': event.location,
        'description': event.description,
        'created_at': event.created_at,
        'updated_at': event.updated_at
    }

    return jsonify(event_data), 200

# Get all events
@event_bp.route('/events', methods=['GET'])
def get_events():
    events = Event.query.all()
    events_list = [{
        'id': event.id,
        'event_name': event.event_name,
        'event_date': event.event_date.strftime('%Y-%m-%d'),
        'location': event.location,
        'description': event.description,
        'created_at': event.created_at,
        'updated_at': event.updated_at
    } for event in events]

    return jsonify(events_list), 200

# Update an event
@event_bp.route('/events/<int:event_id>', methods=['PUT'])
def update_event(event_id):
    event = Event.query.get(event_id)
    if event is None:
        return abort(404, description="Event not found")

    data = request.get_json()

    event.event_name = data.get('event_name', event.event_name)
    event.location = data.get('location', event.location)
    
    if 'event_date' in data:
        try:
            event.event_date = datetime.strptime(data['event_date'], '%Y-%m-%d').date()
        except ValueError:
            return jsonify({'error': 'Invalid date format, expected YYYY-MM-DD'}), 400
    
    event.description = data.get('description', event.description)
    event.updated_at = datetime.utcnow()

    db.session.commit()

    return jsonify({'message': 'Event updated successfully'}), 200

# Delete an event
@event_bp.route('/events/<int:event_id>', methods=['DELETE'])
def delete_event(event_id):
    event = Event.query.get(event_id)
    if event is None:
        return abort(404, description="Event not found")

    db.session.delete(event)
    db.session.commit()

    return jsonify({'message': 'Event deleted successfully'}), 200
