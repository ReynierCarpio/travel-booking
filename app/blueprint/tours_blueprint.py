from flask_smorest import Blueprint
from flask import abort, jsonify
from app.repository.tours_repository import ToursRepository
from app.schema.tours_schema import ToursSchema

tours_blp = Blueprint('tours', 'tours', url_prefix='/tours', description="Operations for Tours")

@tours_blp.route("/", methods=['POST'])
@tours_blp.arguments(ToursSchema)
@tours_blp.response(201, ToursSchema)
def create_tour(data):
    tour = ToursRepository.create_tour(data)
    return tour

@tours_blp.route("/<int:tour_id>", methods=['GET'])
@tours_blp.response(200, ToursSchema)
def get_tour_by_id(tour_id):
    tour = ToursRepository.get_tour_by_id(tour_id)
    if not tour:
        return jsonify({"message": "Tour not found"}), 404
    return tour

@tours_blp.route("/", methods=['GET'])
@tours_blp.response(200, ToursSchema(many=True))
def get_all_tours():
    tours = ToursRepository.get_all_tours()
    return tours

@tours_blp.route("/<int:tour_id>", methods=['PUT'])
@tours_blp.arguments(ToursSchema)
@tours_blp.response(200, ToursSchema)
def update_tour(data, tour_id):
    tour = ToursRepository.get_tour_by_id(tour_id)
    if not tour:
        abort(404, description="Tour not found")
    updated_tour = ToursRepository.update_tour(tour, data)
    return updated_tour

@tours_blp.route("/<int:tour_id>", methods=["DELETE"])
@tours_blp.response(204)
def delete_tour(tour_id):
    tour = ToursRepository.get_tour_by_id(tour_id)
    if not tour:
        abort(404, description="Tour not found")
    ToursRepository.delete_tour(tour)
    return ''
