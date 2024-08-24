from flask import Blueprint, request, jsonify, abort
from api.models import db
from models.payment import Payment, PaymentMethodEnum, PaymentStatusEnum
from datetime import datetime, timezone

# Define a blueprint for payment-related routes
payment_bp = Blueprint('payments', __name__)

# Create a new payment
@payment_bp.route('/payments', methods=['POST'])
def create_payment():
    data = request.get_json()

    # Validate required fields
    if not all(field in data for field in ['amount', 'amount_due', 'payment_method', 'status']):
        return jsonify({'error': 'Missing required fields'}), 400

    try:
        # Validate enums
        payment_method = PaymentMethodEnum(data['payment_method'])
        status = PaymentStatusEnum(data['status'])
    except ValueError:
        return jsonify({'error': 'Invalid payment method or status'}), 400

    # Create the payment
    new_payment = Payment(
        amount=data['amount'],
        amount_due=data['amount_due'],
        payment_method=payment_method,
        status=status
    )

    db.session.add(new_payment)
    db.session.commit()

    return jsonify({'message': 'Payment created successfully', 'payment_id': new_payment.id}), 201

# Get a payment by ID
@payment_bp.route('/payments/<int:payment_id>', methods=['GET'])
def get_payment(payment_id):
    payment = Payment.query.get(payment_id)
    if payment is None:
        return abort(404, description="Payment not found")

    payment_data = {
        'id': payment.id,
        'amount': payment.amount,
        'amount_due': payment.amount_due,
        'payment_date': payment.payment_date,
        'payment_method': payment.payment_method.value,
        'status': payment.status.value
    }

    return jsonify(payment_data), 200

# Get all payments
@payment_bp.route('/payments', methods=['GET'])
def get_payments():
    payments = Payment.query.all()
    payments_list = [{
        'id': payment.id,
        'amount': payment.amount,
        'amount_due': payment.amount_due,
        'payment_date': payment.payment_date,
        'payment_method': payment.payment_method.value,
        'status': payment.status.value
    } for payment in payments]

    return jsonify(payments_list), 200

# Update a payment
@payment_bp.route('/payments/<int:payment_id>', methods=['PUT'])
def update_payment(payment_id):
    payment = Payment.query.get(payment_id)
    if payment is None:
        return abort(404, description="Payment not found")

    data = request.get_json()

    if 'amount' in data:
        payment.amount = data['amount']
    if 'amount_due' in data:
        payment.amount_due = data['amount_due']
    
    if 'payment_method' in data:
        try:
            payment.payment_method = PaymentMethodEnum(data['payment_method'])
        except ValueError:
            return jsonify({'error': 'Invalid payment method'}), 400
    
    if 'status' in data:
        try:
            payment.status = PaymentStatusEnum(data['status'])
        except ValueError:
            return jsonify({'error': 'Invalid payment status'}), 400

    payment.payment_date = datetime.now(timezone.utc)

    db.session.commit()

    return jsonify({'message': 'Payment updated successfully'}), 200

# Delete a payment
@payment_bp.route('/payments/<int:payment_id>', methods=['DELETE'])
def delete_payment(payment_id):
    payment = Payment.query.get(payment_id)
    if payment is None:
        return abort(404, description="Payment not found")

    db.session.delete(payment)
    db.session.commit()

    return jsonify({'message': 'Payment deleted successfully'}), 200
