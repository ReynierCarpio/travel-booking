from marshmallow import Schema, fields

class ToursSchema(Schema):
    tour_id = fields.Int(dump_only=True)
    tour_name = fields.Str(required=True)
    description = fields.Str()
    price = fields.Decimal(as_string=True, required=True)
    start_date = fields.Date(required=True)
    end_date = fields.Date(required=True)
    seats_available = fields.Int(required=True)
    image_url = fields.Str()
    created_at = fields.DateTime(dump_only=True)
    updated_at = fields.DateTime(dump_only=True)
    deleted_at = fields.DateTime(dump_only=True)
