from app.extension import db
from app.models.tours_model import ToursModel
from datetime import datetime

class ToursRepository:

    @staticmethod
    def create_tour(data):
        tour = ToursModel(**data)
        db.session.add(tour)
        db.session.commit()
        return tour

    @staticmethod
    def get_tour_by_id(tour_id):
        return ToursModel.query.get(tour_id)

    @staticmethod
    def get_all_tours():
        return ToursModel.query.filter_by(deleted_at=None).all()

    @staticmethod
    def update_tour(tour, data):
        for key, value in data.items():
            setattr(tour, key, value)
        tour.updated_at = datetime.utcnow()
        db.session.commit()
        return tour

    @staticmethod
    def delete_tour(tour):
        tour.deleted_at = datetime.utcnow()
        db.session.commit()
