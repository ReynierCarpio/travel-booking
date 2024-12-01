from flask_smorest import Blueprint
from flask import abort, jsonify
from app.repository.admin_logs_repository import AdminLogsRepository
from app.schema.admin_logs_schema import AdminLogsSchema

admin_logs_blp = Blueprint(
    'admin_logs',
    'admin_logs',
    url_prefix='/admin-logs',
    description="Operations for Admin Logs"
)

# Create a new admin log
@admin_logs_blp.route("/", methods=["POST"])
@admin_logs_blp.arguments(AdminLogsSchema)
@admin_logs_blp.response(201, AdminLogsSchema)
def create_admin_log(data):
    return AdminLogsRepository.create_log(data)

# Get all admin logs
@admin_logs_blp.route("/", methods=["GET"])
@admin_logs_blp.response(200, AdminLogsSchema(many=True))
def get_all_admin_logs():
    return AdminLogsRepository.get_all_logs()

# Get a specific admin log by ID
@admin_logs_blp.route("/<int:log_id>", methods=["GET"])
@admin_logs_blp.response(200, AdminLogsSchema)
def get_admin_log_by_id(log_id):
    log = AdminLogsRepository.get_log_by_id(log_id)
    if not log:
        return jsonify({"message": "Log not found"}), 404
    return log

# Update a specific admin log
@admin_logs_blp.route("/<int:log_id>", methods=["PUT"])
@admin_logs_blp.arguments(AdminLogsSchema)
@admin_logs_blp.response(200, AdminLogsSchema)
def update_admin_log(data, log_id):
    log = AdminLogsRepository.get_log_by_id(log_id)
    if not log:
        abort(404, description="Log not found")
    return AdminLogsRepository.update_log(log, data)

# Delete a specific admin log
@admin_logs_blp.route("/<int:log_id>", methods=["DELETE"])
@admin_logs_blp.response(204)
def delete_admin_log(log_id):
    log = AdminLogsRepository.get_log_by_id(log_id)
    if not log:
        abort(404, description="Log not found")
    AdminLogsRepository.delete_log(log)
    return ''
