from marshmallow import Schema, fields

class ReviewsSchema(Schema):
    review_id = fields.Int(dump_only=True)
    user_id = fields.Int(required=True)  # ForeignKey to User
    tour_id = fields.Int(required=True)  # ForeignKey to Tours
    rating = fields.Int(required=True)
    comment = fields.Str()
    created_at = fields.DateTime(dump_only=True)
