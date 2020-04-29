# web_app/routes/recommendation_routes.py

from flask import Blueprint, jsonify, request, render_template, flash, redirect
from web_app.models import Strain, parse_records

recommendation_routes = Blueprint("recommendation_routes", __name__)

@recommendation_routes.route("/recommendation_form")
def strain_recommendation_form():
    return render_template("recommendation_form.html")


@recommendation_routes.route("/strains/recommendation", methods=["POST"])
def strain_prediction():
    strain_type = request.form.getlist("strain_type")
    feelings_relief = request.form.getlist("feelings/relief")
    flavors = request.form.getlist("flavors")
	
    print(strain_type)
    print(feelings_relief)
    print(flavors)

    results = (Strain.query.filter(Strain.strain_type.in_(strain_type))
               .filter(Strain.strain_relief_profile.in_(feelings_relief))
               .filter(Strain.strain_flavor_profile.in_(flavors))).all()
    
    print(results)
    
    recommended = parse_records(results)
    print(recommended)
    return jsonify(recommended)