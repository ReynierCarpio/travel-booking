from app.extension import db
from sqlalchemy.orm import relationship

class PaymentModel(db.Model):
    __tablename__ = "payment"

    payment_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    booking_id = db.Column(db.Integer, db.ForeignKey('bookings.booking_id', ondelete='CASCADE'), nullable=False)
    payment_date = db.Column(db.DateTime, nullable=False)
    amount = db.Column(db.Numeric(10, 2), nullable=False)
    payment_method = db.Column(db.Enum('GCASH'), nullable=False)
    payment_status = db.Column(db.Enum('SUCCESS', 'FAILED'), nullable=False)
    transaction_id = db.Column(db.String(100))

    # Relationships
    booking = relationship('BookingsModel', back_populates='payment')
