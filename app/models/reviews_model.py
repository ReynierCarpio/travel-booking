from app.extension import db
from sqlalchemy.orm import relationship

class ReviewsModel(db.Model):
    __tablename__ = "reviews"

    review_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.user_id', ondelete='CASCADE'), nullable=False)
    tour_id = db.Column(db.Integer, db.ForeignKey('tours.tour_id', ondelete='CASCADE'), nullable=False)
    rating = db.Column(db.Integer, nullable=False)
    comment = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())

    # Relationships
    user = relationship('UserModel', back_populates='reviews')
    tour = relationship('ToursModel', back_populates='reviews')
