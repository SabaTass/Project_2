import pandas as pd
import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine

from flask import Flask, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy

from config import crash
app = Flask(__name__, static_url_path="/static")

DB_URI= crash
#################################################
# Database Setup
#################################################

app.config["SQLALCHEMY_DATABASE_URI"] = DB_URI
db = SQLAlchemy(app)

# reflect an existing database into a new model
Base = automap_base()

# reflect the tables
Base.prepare(db.engine, reflect=True)
# Save references to each table
car_crash_table = Base.classes.car_crash

#View Routes
@app.route("/")
def index():
    """Return the homepage."""
    return render_template("index.html")

@app.route("/Maps")
def Maps():
    """Return a list of Maps."""
    return render_template("Maps.html")
@app.route("/charts")
def charts():
    return render_template("charts.html")

@app.route("/API/car_crash")
def car_crash_data():
    sel = [
        car_crash_table.county_name,
        car_crash_table.fatal,
        car_crash_table.peds,
        car_crash_table.persons,
        car_crash_table.st_case,
        car_crash_table.total_vehicles,
        car_crash_table.date,
        car_crash_table.year,
        car_crash_table.month,
        car_crash_table.time
    ]

    results = db.session.query(*sel).all()

    # Create a dictionary entry for each row of metadata information
    # create a dictionary for each row of comparison data
    comparison_data = {
        
        "county_name": [result[0] for result in results],
        "fatal": [result[1] for result in results],
        "Pedestrian" : [result[2] for result in results],
        "Persons" : [result[3] for result in results],
        "st_case" : [result[4] for result in results],
        "Total_Vehciles_involved": [result[5] for result in results],
        "Date":[result[6] for result in results],
        "Year":[result[7] for result in results],
        "Month":[result[8] for result in results],
        "time":[result[9] for result in results]
    }
    # jsonify the dictionary
    return jsonify(comparison_data)

if __name__ == "__main__":
    app.run(debug=True)