from marshmallow import Schema, fields

class UserSchema(Schema):
    user_id = fields.Int(dump_only=True)
    username = fields.Str(required=True)
    password_hash = fields.Str(required=True, load_only=True)
    email = fields.Email(required=True)
    phone_number = fields.Str()
    first_name = fields.Str()
    last_name = fields.Str()
    user_role = fields.Str(required=True)
    created_at = fields.DateTime(dump_only=True)
    updated_at = fields.DateTime(dump_only=True)
    deleted_at = fields.DateTime(dump_only=True)
