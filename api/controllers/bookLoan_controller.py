from flask import Blueprint, request, jsonify, abort
from . import db
from models.bookLoan import BookLoan, BookLoanEnum
from datetime import datetime

# Define a blueprint for book loan-related routes
book_loan_bp = Blueprint('book_loans', __name__)

# Create a new book loan
@book_loan_bp.route('/book_loans', methods=['POST'])
def create_book_loan():
    data = request.get_json()

    # Validate required fields
    if not all(field in data for field in ['student_id', 'book_id']):
        return jsonify({'error': 'Missing required fields'}), 400

    # Create the book loan
    new_loan = BookLoan(
        student_id=data['student_id'],
        book_id=data['book_id'],
        borrow_date=datetime.utcnow(),
        status=BookLoanEnum.borrowed
    )

    db.session.add(new_loan)
    db.session.commit()

    return jsonify({'message': 'Book loan created successfully', 'loan_id': new_loan.id}), 201

# Get a book loan by ID
@book_loan_bp.route('/book_loans/<int:loan_id>', methods=['GET'])
def get_book_loan(loan_id):
    book_loan = BookLoan.query.get(loan_id)
    if book_loan is None:
        return abort(404, description="Book loan not found")

    book_loan_data = {
        'id': book_loan.id,
        'borrow_date': book_loan.borrow_date,
        'return_date': book_loan.return_date,
        'status': book_loan.status.value,
        'student_id': book_loan.student_id,
        'book_id': book_loan.book_id
    }

    return jsonify(book_loan_data), 200

# Get all book loans
@book_loan_bp.route('/book_loans', methods=['GET'])
def get_book_loans():
    book_loans = BookLoan.query.all()
    loans_list = [{
        'id': loan.id,
        'borrow_date': loan.borrow_date,
        'return_date': loan.return_date,
        'status': loan.status.value,
        'student_id': loan.student_id,
        'book_id': loan.book_id
    } for loan in book_loans]

    return jsonify(loans_list), 200

# Update a book loan (status or return date)
@book_loan_bp.route('/book_loans/<int:loan_id>', methods=['PUT'])
def update_book_loan(loan_id):
    book_loan = BookLoan.query.get(loan_id)
    if book_loan is None:
        return abort(404, description="Book loan not found")

    data = request.get_json()

    if 'status' in data:
        try:
            book_loan.status = BookLoanEnum(data['status'])
        except ValueError:
            return jsonify({'error': 'Invalid status value'}), 400

    if book_loan.status == BookLoanEnum.returned and not book_loan.return_date:
        book_loan.return_date = datetime.utcnow()

    db.session.commit()

    return jsonify({'message': 'Book loan updated successfully'}), 200

# Delete a book loan
@book_loan_bp.route('/book_loans/<int:loan_id>', methods=['DELETE'])
def delete_book_loan(loan_id):
    book_loan = BookLoan.query.get(loan_id)
    if book_loan is None:
        return abort(404, description="Book loan not found")

    db.session.delete(book_loan)
    db.session.commit()

    return jsonify({'message': 'Book loan deleted successfully'}), 200
