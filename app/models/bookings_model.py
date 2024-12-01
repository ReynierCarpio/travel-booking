from app.extension import db
from sqlalchemy.orm import relationship

class BookingsModel(db.Model):
    __tablename__ = "bookings"

    booking_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.user_id', ondelete='CASCADE'), nullable=False)
    tour_id = db.Column(db.Integer, db.ForeignKey('tours.tour_id', ondelete='CASCADE'), nullable=False)
    booking_date = db.Column(db.DateTime, nullable=False)
    travel_date = db.Column(db.Date, nullable=False)
    seats_booked = db.Column(db.Integer, nullable=False)
    total_amount = db.Column(db.Numeric(10, 2), nullable=False)
    payment_status = db.Column(db.Enum('SUCCESS', 'FAILED'), nullable=False)
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())
    updated_at = db.Column(db.DateTime, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())

    # Relationships
    user = relationship('UserModel', back_populates='bookings')
    tour = relationship('ToursModel', back_populates='bookings')
    payment = relationship('PaymentModel', back_populates='booking', uselist=False)
