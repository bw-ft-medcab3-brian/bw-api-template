# web_app/routes/recommendation_routes.py

from flask import Blueprint, jsonify, request, render_template, flash, redirect
from web_app.models import Strain, parse_records
import pandas as pd
from random import sample

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

    print(type(strain_type))
    print(type(feelings_relief))
    print(type(flavors))
  
    # results_type_feelings = Strain.query.filter(Strain.strain_type.in_(strain_type) & (Strain.strain_relief_profile.in_(feelings_relief))).all()
    # results_type_flavor = Strain.query.filter(Strain.strain_type.in_(strain_type) & (Strain.strain_flavor_profile.in_(flavors))).all()
    # results_flavor_feelings = Strain.query.filter(Strain.strain_flavor_profile.in_(flavors) & (Strain.strain_relief_profile.in_(feelings_relief))).all()

    # print(results_type_feelings)
    # print(results_type_flavor)
    # print(results_flavor_feelings)


    flavor_results = []
    for flavor in flavors:
        flavor_results.append(Strain.query.filter(Strain.strain_flavor_profile.like(f'%{flavor}%')).all())
    
    flavor_results = flavor_results[0]

    strain_results = []
    for strain in strain_type:
        strain_results.append(Strain.query.filter(Strain.strain_type.like(f'%{strain}%')).all())

    strain_results = strain_results[0]

    feelings_relief_results = []
    for feeling in feelings_relief:
        feelings_relief_results.append(Strain.query.filter(Strain.strain_relief_profile.like(f'%{feeling}%')).all())

    feelings_relief_results = feelings_relief_results[0]

    flavor_strains = []
    for flavor in flavor_results:
        flavor_strains.append(flavor.strain_name)

    strains_strains = []
    for strain in strain_results:
        strains_strains.append(strain.strain_name)

    relief_strains = []
    for relief in feelings_relief_results:
        relief_strains.append(relief.strain_name) 

      

    # Python program to illustrate the intersection 
    # of two lists using set() method 
    # def intersection(lst1, lst2): 
    #    return list(set(lst1) & set(lst2))
    
    # intersection1_list = []
    # intersection1 = set(flavor_strains + strains_strains + relief_strains)
    
    intersection_list = list(set(flavor_strains) & set(strains_strains))
    intersection_list2 = list(set(flavor_strains) & set(relief_strains))
    intersection_list3 = list(set(strains_strains) & set(relief_strains))

    recommended_list = [intersection_list, intersection_list2, intersection_list3]
    
    for record in recommended_list:
        for i in range(len(record)):
            if len(record[i]) == 0:
                return("Please try a new combination. No strains found.")
            else:
                return jsonify(record)