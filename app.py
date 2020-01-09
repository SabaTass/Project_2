import pandas as pd
import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()
from flask import Flask, jsonify, render_template
import json
from sqlalchemy import create_engine, func, inspect
from flask import Flask, jsonify
import datetime as dt

# from config import crash
app = Flask(__name__, static_url_path="/static")
# DB_URI= crash
#################################################
# Database Setup
#################################################
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# crash_db = 'postgresql:saba123@localhost:5432/crash'
# engine = create_engine(f'postgresql://{crash_db}')
engine = create_engine('postgresql://postgres:MyPostSql2day@127.0.0.1:5432/crash_db')
connection = engine.connect()
################################################
Base = automap_base()
Base.prepare(engine, reflect=True)
Base.classes.keys()
################################################
FatalsbyCounty = Base.classes.fatalsbycounty
session = Session(engine)
#View Routes
@app.route("/")
def index():
    """Return the homepage."""
    return render_template("index.html")
@app.route("/maps")
def Maps():
    """Return a list of Maps."""
    return render_template("maps.html")
@app.route("/data")
def data():
    """Return a list of Maps."""
    return render_template("data.html")
@app.route("/charts")
def charts():
    return render_template("charts.html")
@app.route("/API/NC_Fatal_byCounty")
def fatal_county():
    car_data = engine.execute('select * from fatalsbycounty').fetchall()
    session.close()
    nccountyfatal = [] 
    for county, fatals, peds, persons, vehicles in car_data:
        car= {}
        car['County']=county
        car['Fatals']=fatals
        car['Peds']=peds
        car['Persons']=persons
        car['Total_vehicles']=vehicles
        nccountyfatal.append(car)
        # newncc = nccountyfatal[0]
    #Return a Json Dictionary
    return jsonify(nccountyfatal)
@app.route("/API/NC_Fatal_byHour")
def fatal_hour():
    hour_data = engine.execute('select * from fatalsbyhour').fetchall()
    session.close()
    nchourfatal = [] 
    for hour, fatals, peds, persons, vehicles in hour_data:
        hr= {}
        hr['Hour']=hour
        hr['Fatals']=fatals
        hr['Peds']=peds
        hr['Persons']=persons
        hr['Total_vehicles']=vehicles

        nchourfatal.append(hr)
    #Return a Json Dictionary

    total_hour = nchourfatal
    return jsonify(total_hour)
@app.route("/API/NC_Fatal_byMonth")
def fatal_month():
    month_data = engine.execute('select * from fatalsbymonth').fetchall()
    session.close()
    ncmonthfatal = [] 
    for month, fatals, peds, persons, vehicles in month_data:
        mth= {}
        mth['Month']=month
        mth['Fatals']=fatals
        mth['Peds']=peds
        mth['Persons']=persons
        mth['Total_vehicles']=vehicles
        ncmonthfatal.append(mth)
    
    #Return a Json Dictionary
    return jsonify(ncmonthfatal)
@app.route("/API/Wake_Fatals_map")
def wake_fatals_map():
    wake_map = engine.execute('select * from wakecountyfatals').fetchall()
    session.close()
    wakefatalmap = [] 
    for index, county, year, fatals, latitude, longitude, totalvehicles in wake_map:
        wfm= {}
        wfm['Index']=index
        wfm['County']=county
        wfm['Year']=year
        wfm['Fatals']=fatals
        wfm['Latitude']=latitude
        wfm['Longitude']=longitude
        wfm['Total_vehicles']=totalvehicles
        
        wakefatalmap.append(wfm)
    
    #Return a Json Dictionary
    return jsonify(wakefatalmap)
if __name__ == "__main__":
    app.run(debug=True)