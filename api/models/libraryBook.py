from api.models import db
import enum
from sqlalchemy_serializer import SerializerMixin

class AvailabilityEnum(enum.Enum):
    Available = 'Available'
    Checked_out = 'Checked Out'
    Reserved = 'Reserved'

class LibraryBook(db.Model, SerializerMixin):
    __tablename__ = 'library_books'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    author = db.Column(db.String(100), nullable=False)
    isbn = db.Column(db.String(13), nullable=False)
    availability = db.Column(db.Enum(AvailabilityEnum), default=AvailabilityEnum.Available, nullable=False)

    # Relationships
    book_loans = db.relationship('BookLoan', back_populates='book', cascade='all, delete-orphan')

    def __repr__(self):
        return f'<LibraryBook id={self.id}, title={self.title}, author={self.author}, isbn={self.isbn}, availability={self.availability.value}>'
