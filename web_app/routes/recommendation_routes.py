# web_app/routes/recommendation_routes.py

from flask import Blueprint, jsonify, request, render_template, flash, redirect

recommendation_routes = Blueprint("recommendation_routes", __name__)

@recommendation_routes.route("/recommendation_form")
def strain_recommendation_form():
    return render_template("recommendation_form.html")


@recommendation_routes.route("/strains/predict", methods=["POST"])
def strain_prediction():
    strain_type = request.form.getlist("strain_type")
    feelings_wanted = request.form.getlist("feelings_wanted")
    feelings_avoid = request.form.getlist("feelings_avoid")
    symptom_relief = request.form.getlist("symptom_relief")
    flavors = request.form.getlist("flavors")
	
    dict_of_inputs = {"strainType": strain_type, "feelingsWanted": feelings_wanted,
                      "feelingsAvoid": feelings_avoid, "symptomRelief": symptom_relief,
                      "flavors": flavors}
	
    return dict_of_inputs