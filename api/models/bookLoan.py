from api.models import db
import enum
from datetime import datetime

class BookLoanEnum(enum.Enum):
    borrowed = 'borrowed'
    returned = 'returned'
    overdue = 'overdue'

class BookLoan(db.Model):
    __tablename__ = 'book_loans'

    id = db.Column(db.Integer, primary_key=True)
    borrow_date = db.Column(db.Date, default=datetime.utcnow, nullable=False) 
    return_date = db.Column(db.Date, nullable=True)
    status = db.Column(db.Enum(BookLoanEnum), default=BookLoanEnum.borrowed, nullable=False)
    student_id = db.Column(db.Integer, db.ForeignKey('students.id'), nullable=False)
    book_id = db.Column(db.Integer, db.ForeignKey('library_books.id'), nullable=False)

    def __repr__(self):
        return f'<BookLoan id={self.id}, borrow_date={self.borrow_date}, return_date={self.return_date}, status={self.status.value}>'
