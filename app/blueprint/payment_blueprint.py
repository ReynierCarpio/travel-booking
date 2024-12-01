from flask_smorest import Blueprint
from flask import abort, jsonify
from app.repository.payment_repository import PaymentRepository
from app.schema.payment_schema import PaymentSchema


payment_blp = Blueprint('payments', 'payments', url_prefix='/payments', description="Operations for Payments")

@payment_blp.route("/", methods=['POST'])
@payment_blp.arguments(PaymentSchema)
@payment_blp.response(201, PaymentSchema)
def create_payment(data):
    payment = PaymentRepository.create_payment(data)
    return payment

@payment_blp.route("/<int:payment_id>", methods=['GET'])
@payment_blp.response(200, PaymentSchema)
def get_payment_by_id(payment_id):
    payment = PaymentRepository.get_payment_by_id(payment_id)
    if not payment:
        return {"message": "Payment not found"}, 404
    return payment

@payment_blp.route("/", methods=['GET'])
@payment_blp.response(200, PaymentSchema(many=True))
def get_all_payments():
    payments = PaymentRepository.get_payments_by_booking(None)
    return payments

@payment_blp.route("/<int:payment_id>", methods=["DELETE"])
@payment_blp.response(204)
def delete_payment(payment_id):
    payment = PaymentRepository.get_payment_by_id(payment_id)
    if not payment:
        abort(404, description="Payment not found")
    PaymentRepository.delete_payment(payment)
    return ''