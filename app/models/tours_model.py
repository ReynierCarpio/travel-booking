from app.extension import db
from sqlalchemy.orm import relationship

class ToursModel(db.Model):
    __tablename__ = "tours"

    tour_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    tour_name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)
    price = db.Column(db.Numeric(10, 2), nullable=False)
    start_date = db.Column(db.Date, nullable=False)
    end_date = db.Column(db.Date, nullable=False)
    seats_available = db.Column(db.Integer, nullable=False)
    image_url = db.Column(db.String(255))
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())
    updated_at = db.Column(db.DateTime, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())
    deleted_at = db.Column(db.DateTime, nullable=True)

    # Relationships
    bookings = relationship('BookingsModel', back_populates='tour', cascade="all, delete-orphan")
    reviews = relationship('ReviewsModel', back_populates='tour', cascade="all, delete-orphan")
