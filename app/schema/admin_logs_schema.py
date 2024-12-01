from marshmallow import Schema, fields

class AdminLogsSchema(Schema):
    log_id = fields.Int(dump_only=True)
    admin_id = fields.Int(required=True)  # ForeignKey to User (Admin)
    action_type = fields.Str(required=True)
    description = fields.Str()
    timestamp = fields.DateTime(dump_only=True)
