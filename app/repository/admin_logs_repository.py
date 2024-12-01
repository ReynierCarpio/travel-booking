from datetime import datetime
from app.extension import db
from app.models.admin_logs_model import AdminLogsModel

class AdminLogsRepository:

    @staticmethod
    def create_log(data):
        log = AdminLogsModel(**data)
        db.session.add(log)
        db.session.commit()
        return log

    @staticmethod
    def get_log_by_id(log_id):
        return AdminLogsModel.query.get(log_id)

    @staticmethod
    def get_all_logs():
        return AdminLogsModel.query.all()

    @staticmethod
    def update_log(log, data):
        for key, value in data.items():
            setattr(log, key, value)
        db.session.commit()
        return log

    @staticmethod
    def delete_log(log):
        db.session.delete(log)
        db.session.commit()
