from api.models import db
import enum

class AvailabilityEnum(enum.Enum):
    available = 'Available'
    checked_out = 'Checked Out'
    reserved = 'Reserved'

class LibraryBook(db.Model):
    __tablename__ = 'library_books'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    author = db.Column(db.String(100), nullable=False)
    isbn = db.Column(db.String(13), nullable=False)
    availability = db.Column(db.Enum(AvailabilityEnum), default=AvailabilityEnum.available, nullable=False)

    def __repr__(self):
        return f'<LibraryBook id={self.id}, title={self.title}, author={self.author}, isbn={self.isbn}, availability={self.availability.value}>'
