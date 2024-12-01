from marshmallow import Schema, fields

class BookingsSchema(Schema):
    booking_id = fields.Int(dump_only=True)
    user_id = fields.Int(required=True)  # ForeignKey to User
    tour_id = fields.Int(required=True)  # ForeignKey to Tours
    booking_date = fields.DateTime(required=True)
    travel_date = fields.Date(required=True)
    seats_booked = fields.Int(required=True)
    total_amount = fields.Decimal(as_string=True, required=True)
    payment_status = fields.Str(required=True)
    created_at = fields.DateTime(dump_only=True)
    updated_at = fields.DateTime(dump_only=True)
