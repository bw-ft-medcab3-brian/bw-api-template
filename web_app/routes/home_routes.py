# web_app/routes/home_routes.py

from flask import Blueprint, jsonify
from web_app.models import Strain, db, parse_records

home_routes = Blueprint("home_routes", __name__)

@home_routes.route("/")

def welcome():
    return "WELCOME!"

@home_routes.route("/strains.json")

def index():
    strain_records = Strain.query.all()
    strains = parse_records(strain_records)
    return jsonify(strains)
