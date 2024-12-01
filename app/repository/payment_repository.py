from app.extension import db
from app.models.payment_model import PaymentModel

class PaymentRepository:

    @staticmethod
    def create_payment(data):
        payment = PaymentModel(**data)
        db.session.add(payment)
        db.session.commit()
        return payment

    @staticmethod
    def get_payment_by_id(payment_id):
        return PaymentModel.query.get(payment_id)

    @staticmethod
    def get_payments_by_booking(booking_id):
        return PaymentModel.query.filter_by(booking_id=booking_id).all()

    @staticmethod
    def update_payment(payment, data):
        for key, value in data.items():
            setattr(payment, key, value)
        db.session.commit()
        return payment

    @staticmethod
    def delete_payment(payment):

        db.session.delete(payment)
        db.session.commit()
        return True