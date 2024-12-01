from app.extension import db
from sqlalchemy.orm import relationship

class AdminLogsModel(db.Model):
    __tablename__ = "admin_logs"

    log_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    admin_id = db.Column(db.Integer, db.ForeignKey('user.user_id', ondelete='CASCADE'), nullable=False)
    action_type = db.Column(db.Enum('ADD', 'DELETE', 'UPDATE'), nullable=False)
    description = db.Column(db.Text)
    timestamp = db.Column(db.DateTime, default=db.func.current_timestamp())

    # Relationships
    admin = relationship('UserModel', back_populates='admin_logs')
