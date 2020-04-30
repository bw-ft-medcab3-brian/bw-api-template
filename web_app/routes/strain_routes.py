import pandas as pd
from flask import Blueprint, jsonify, request, render_template, flash, redirect
from web_app.models import Strain, db, migrate
from web_app.services.strain_service import strains
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY")

strain_routes = Blueprint("strain_routes", __name__)
@strain_routes.route("/strain-db-update")
def strain_update():
    df = pd.DataFrame(strains)

    for index, row in df.iterrows():
        strain = Strain(strain_description=str(row["Strain_description"]),
                        strain_flavor_profile=str(row["flavors"]),
                        strain_relief_profile=str(row["feelings_symptoms"]),
                        strain_name=str(row["strain"]),
                        strain_type=str(row["strain_type"]))
        db.session.add(strain)
    db.session.commit()
    return "Strain DB Update Successful"


@strain_routes.route('/db-refresh')
def refresh():
    print("URL PARMS", dict(request.args))
    if "api_key" in dict(request.args) and request.args["api_key"] == API_KEY:
        print(type(db))
        db.drop_all()
        db.create_all()

        strain_update()
        return jsonify({"message": "DB RESET OK"})
    else:
        flash("OOPS Permission Denied", "danger")
        return redirect("/recommendation_form")
