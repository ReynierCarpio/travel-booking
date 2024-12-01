from flask_smorest import Blueprint
from flask import abort, jsonify
from app.repository.reviews_repository import ReviewsRepository
from app.schema.reviews_schema import ReviewsSchema

reviews_blp = Blueprint('reviews', 'reviews', url_prefix='/reviews', description="Operations for Reviews")

@reviews_blp.route("/", methods=['POST'])
@reviews_blp.arguments(ReviewsSchema)
@reviews_blp.response(201, ReviewsSchema)
def create_review(data):
    review = ReviewsRepository.create_review(data)
    return review

@reviews_blp.route("/<int:review_id>", methods=['GET'])
@reviews_blp.response(200, ReviewsSchema)
def get_review_by_id(review_id):
    review = ReviewsRepository.get_review_by_id(review_id)
    if not review:
        return {"message": "Review not found"}, 404
    return review

@reviews_blp.route("/", methods=['GET'])
@reviews_blp.response(200, ReviewsSchema(many=True))
def get_all_reviews():
    reviews = ReviewsRepository.get_reviews_by_tour(None)
    return reviews

@reviews_blp.route("/<int:review_id>", methods=["DELETE"])
@reviews_blp.response(204)
def delete_review(review_id):
    review = ReviewsRepository.get_review_by_id(review_id)
    if not review:
        abort(404, description="Review not found")
    ReviewsRepository.delete_review(review)
    return ''