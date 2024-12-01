from app.extension import db
from app.models.bookings_model import BookingsModel
from datetime import datetime

class BookingsRepository:

    @staticmethod
    def create_booking(data):
        booking = BookingsModel(**data)
        db.session.add(booking)
        db.session.commit()
        return booking

    @staticmethod
    def get_booking_by_id(booking_id):
        return BookingsModel.query.get(booking_id)

    @staticmethod
    def get_all_bookings():
        return BookingsModel.query.filter_by().all()

    @staticmethod
    def get_bookings_by_user(user_id):
        return BookingsModel.query.filter_by(user_id=user_id).all()

    @staticmethod
    def update_booking(booking, data):
        for key, value in data.items():
            setattr(booking, key, value)
        booking.updated_at = datetime.utcnow()
        db.session.commit()
        return booking

    @staticmethod
    def delete_booking(booking):
        booking.deleted_at = datetime.utcnow()
        db.session.commit()
