from flask import Blueprint, jsonify, request, render_template, flash, redirect
from web_app.models import Strain, db, migrate
from web_app.services.strain_service import strains

strain_routes = Blueprint("strain_routes", __name__)
@strain_routes.route("/strain-db-update")
def strain_update():
    for strain in strains:
        strain = Strain(strain_description=strain["strain_description"],
                        strain_flavor_profile=strain["strain_flavor_profile"],
                        strain_frangrance_profile=strain["strain_frangrance_profile"],
                        strain_image=strain["strain_image"],
                        strain_name=strain["strain_name"],
                        strain_nearest_neighbors=strain["strain_nearest_neighbors"],
                        strain_review_key=strain["strain_review_key"],
                        strain_terpene_profile=strain["strain_terpene_profile"],
                        strain_type=strain["strain_type"])
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





