import pandas as pd
from flask import Blueprint, jsonify, request, render_template, flash, redirect
from web_app.models import Strain, db, migrate
from web_app.services.strain_service import strains

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
    """Pull fresh data from Open AQ and replace existing data."""
    db.drop_all()
    db.create_all()
    # TODO Get data from OpenAQ, make Record objects with it, and add to db

    strain_update()

    """data_to_input = strains
    for i in range(len(strains)):
        DB_record = Record(id=i)
        DB_record.datetime = data_to_input[i][0]
        DB_record.value =data_to_input[i][1]
        DB.session.add(DB_record)
    DB.session.commit()"""

    return 'Table refreshed!'





