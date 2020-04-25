# web_app/__init__.py
import os
from dotenv import load_dotenv
from flask import Flask

from web_app.routes.home_routes import home_routes
from web_app.routes.recommendation_routes import recommendation_routes

from web_app.models import db, migrate

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")
SECRET_KEY = os.getenv("SECRET_KEY", default="super secret")

def create_app():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = SECRET_KEY

    app.register_blueprint(home_routes)
    app.register_blueprint(recommendation_routes)

    # TODO
    # configure the database

    return app

if __name__ == "__main__":
    my_app = create_app()
    my_app.run(debug=True)