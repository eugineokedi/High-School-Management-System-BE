from api.models import db
import enum
from datetime import datetime, timezone
from sqlalchemy_serializer import SerializerMixin

class PaymentMethodEnum(enum.Enum):
    M_pesa = 'M_pesa'
    Credit_card = 'Credit_card'
    Bank_transfer = 'Bank_transfer'

class PaymentStatusEnum(enum.Enum):
    Paid = 'Paid'
    Pending = 'Pending'
    Not_paid = 'Not_paid'
    

class Payment(db.Model, SerializerMixin):
    __tablename__ = 'payments'

    id = db.Column(db.Integer, primary_key=True)
    amount = db.Column(db.Float, nullable=False)
    amount_due = db.Column(db.Float, nullable=False)
    payment_date = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc), nullable=False)
    payment_method = db.Column(db.Enum(PaymentMethodEnum), nullable=False)
    status = db.Column(db.Enum(PaymentStatusEnum), nullable=False)
    student_id = db.Column(db.Integer, db.ForeignKey('students.id'), nullable=False)

    # Relationships
    student = db.relationship('Student', back_populates='payments')

    def __repr__(self):
        return f'<Payment id={self.id}, amount={self.amount}, amount_due={self.amount_due}, payment_date={self.payment_date}, payment_method={self.payment_method.value}, status={self.status.value}>'
