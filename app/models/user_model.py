from app.extension import db
from sqlalchemy.orm import relationship
from enum import Enum as Enum

# Define the Enum class
class UserRoleEnum(Enum):
    ADMIN = "ADMIN"
    USERS = "USERS"

class UserModel(db.Model):
    __tablename__ = "user"

    user_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(50), nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    phone_number = db.Column(db.String(20))
    first_name = db.Column(db.String(50))
    last_name = db.Column(db.String(50))
    user_role = db.Column(db.Enum(UserRoleEnum), nullable=False)
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())
    updated_at = db.Column(db.DateTime, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())
    deleted_at = db.Column(db.DateTime, nullable=True)

    # Relationships
    bookings = relationship('BookingsModel', back_populates='user', cascade="all, delete-orphan")
    reviews = relationship('ReviewsModel', back_populates='user', cascade="all, delete-orphan")
    admin_logs = relationship('AdminLogsModel', back_populates='admin', cascade="all, delete-orphan")