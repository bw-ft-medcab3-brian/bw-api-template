# web_app/routes/recommendation_routes.py

from flask import Blueprint, jsonify, request, render_template, flash, redirect

recommendation_routes = Blueprint("recommendation_routes", __name__)

@recommendation_routes.route("/recommendations.json")
def list_recommendations():
    recommendations = [
        {"id": 1, "strain_name": "Recommendation 1", "strain_type": "hybrid",
         "strain_terpene_profile": "profile type 1", "strain_flavor_profile": "flavor_1",
         "strain_frangrance_profile": "fragrance", "strain_review_key": "review_1",
         "strain_nearest_neighbors": "nearest_1", "strain_description": "description_1",
         "strain_image": "image_1" },

         {"id": 2, "strain_name": "Recommendation 2", "strain_type": "sativa",
         "strain_terpene_profile": "profile type 2", "strain_flavor_profile": "flavor_2",
         "strain_frangrance_profile": "fragrance_2", "strain_review_key": "review_2",
         "strain_nearest_neighbors": "nearest_2", "strain_description": "description_2",
         "strain_image": "image_2" },
        
         {"id": 3, "strain_name": "Recommendation 3", "strain_type": "sativa",
         "strain_terpene_profile": "profile type 3", "strain_flavor_profile": "flavor_3",
         "strain_frangrance_profile": "fragrance_3", "strain_review_key": "review_3",
         "strain_nearest_neighbors": "nearest_3", "strain_description": "description_3",
         "strain_image": "image_3" }]       

    # TODO return ML recommendation using pickle object.
    return jsonify(recommendations)