from api.models import db
import enum
from datetime import datetime, timezone

class PaymentMethodEnum(enum.Enum):
    mpesa = 'M-pesa'
    credit_card = 'Credit card'
    bank_transfer = 'Bank transfer'

class PaymentStatusEnum(enum.Enum):
    paid = 'Paid'
    pending = 'Pending'
    not_paid = 'Not paid'

class Payment(db.Model):
    __tablename__ = 'payments'

    id = db.Column(db.Integer, primary_key=True)
    amount = db.Column(db.Float, nullable=False)
    amount_due = db.Column(db.Float, nullable=False)
    payment_date = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc), nullable=False)
    payment_method = db.Column(db.Enum(PaymentMethodEnum), nullable=False)
    status = db.Column(db.Enum(PaymentStatusEnum), nullable=False)

    def __repr__(self):
        return f'<Payment id={self.id}, amount={self.amount}, amount_due={self.amount_due}, payment_date={self.payment_date}, payment_method={self.payment_method.value}, status={self.status.value}>'
