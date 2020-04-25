# web_app/routes/recommendation_routes.py

from flask import Blueprint, jsonify, request, render_template, flash, redirect

recommendation_routes = Blueprint("recommendation_routes", __name__)

@recommendation_routes.route("/recommendations.json")
def list_recommendations():
    recommendations = [
        {"id": 1, "title": "Recommendation 1"},
        {"id": 2, "title": "Recommendation 2"},
        {"id": 3, "title": "Recommendation 3"},
    ]
    return jsonify(recommendations)