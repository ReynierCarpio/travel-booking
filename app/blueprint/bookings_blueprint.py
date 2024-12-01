from flask_smorest import Blueprint
from flask import abort, jsonify
from app.repository.bookings_repository import BookingsRepository
from app.schema.bookings_schema import BookingsSchema

bookings_blp = Blueprint('bookings', 'bookings', url_prefix='/bookings', description="Operations for Bookings")

@bookings_blp.route("/", methods=['POST'])
@bookings_blp.arguments(BookingsSchema)
@bookings_blp.response(201, BookingsSchema)
def create_booking(data):
    booking = BookingsRepository.create_booking(data)
    return booking

@bookings_blp.route("/<int:booking_id>", methods=['GET'])
@bookings_blp.response(200, BookingsSchema)
def get_booking_by_id(booking_id):
    booking = BookingsRepository.get_booking_by_id(booking_id)
    if not booking:
        return jsonify({"message": "Booking not found"}), 404
    return booking

@bookings_blp.route("/", methods=['GET'])
@bookings_blp.response(200, BookingsSchema(many=True))
def get_all_bookings():
    bookings = BookingsRepository.get_all_bookings()
    return bookings

@bookings_blp.route("/<int:booking_id>", methods=['PUT'])
@bookings_blp.arguments(BookingsSchema)
@bookings_blp.response(200, BookingsSchema)
def update_booking(data, booking_id):
    booking = BookingsRepository.get_booking_by_id(booking_id)
    if not booking:
        abort(404, description="Booking not found")
    updated_booking = BookingsRepository.update_booking(booking, data)
    return updated_booking

@bookings_blp.route("/<int:booking_id>", methods=["DELETE"])
@bookings_blp.response(204)
def delete_booking(booking_id):
    booking = BookingsRepository.get_booking_by_id(booking_id)
    if not booking:
        abort(404, description="Booking not found")
    BookingsRepository.delete_booking(booking)
    return ''
