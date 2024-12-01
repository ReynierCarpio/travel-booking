from app.extension import db
from app.models.reviews_model import ReviewsModel
from datetime import datetime

class ReviewsRepository:

    @staticmethod
    def create_review(data):
        review = ReviewsModel(**data)
        db.session.add(review)
        db.session.commit()
        return review

    @staticmethod
    def get_review_by_id(review_id):
        return ReviewsModel.query.get(review_id)

    @staticmethod
    def get_reviews_by_tour(tour_id):
        return ReviewsModel.query.filter_by(tour_id=tour_id).all()

    @staticmethod
    def get_reviews_by_user(user_id):
        return ReviewsModel.query.filter_by(user_id=user_id).all()

    @staticmethod
    def update_review(review, data):
        for key, value in data.items():
            setattr(review, key, value)
        review.updated_at = datetime.utcnow()
        db.session.commit()
        return review

    @staticmethod
    def delete_review(review):
        review.deleted_at = datetime.utcnow()
        db.session.commit()
