from flask import Flask, jsonify
from flask_smorest import Api


# Import blueprints
from app.blueprint.user_blueprint import user_blp
from app.blueprint.tours_blueprint import tours_blp
from app.blueprint.bookings_blueprint import bookings_blp
from app.blueprint.payment_blueprint import payment_blp
from app.blueprint.reviews_blueprint import reviews_blp
from app.blueprint.admin_logs_blueprint import admin_logs_blp
from app.extension import db, migrate
from config import Config
from app.models import user_model
from app.models import tours_model
from app.models import bookings_model
from app.models import payment_model
from app.models import reviews_model
from app.models import admin_logs_model



def create_app():
    """Factory function to create and configure the Flask app."""
    app = Flask(__name__)
    app.config.from_object(Config)

    # Load configuration
    app.config.from_object("config.Config")

    # Initialize extensions
    db.init_app(app)
    migrate.init_app(app, db)

    # Set up Flask-Smorest API
    api = Api(app)
    api.register_blueprint(user_blp)
    api.register_blueprint(tours_blp)
    api.register_blueprint(bookings_blp)
    api.register_blueprint(payment_blp)
    api.register_blueprint(reviews_blp)
    api.register_blueprint(admin_logs_blp)

    # Add a simple home route
    @app.route('/')
    def home():
        return jsonify({"message": "Welcome to the Travel Booking API!"})

    return app
