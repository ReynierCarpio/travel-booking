from marshmallow import Schema, fields

class PaymentSchema(Schema):
    payment_id = fields.Int(dump_only=True)
    booking_id = fields.Int(required=True)  # ForeignKey to Bookings
    payment_date = fields.DateTime(required=True)
    amount = fields.Decimal(as_string=True, required=True)
    payment_method = fields.Str(required=True)
    payment_status = fields.Str(required=True)
    transaction_id = fields.Str()
