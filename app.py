# Import SQLAlchemy `automap` and other dependencies here
from models import create_classes
import os
from flask import (
    Flask,
    render_template,
    jsonify,
    request,
    redirect)

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, inspect, func
import psycopg2

#################################################
# Flask Setup
#################################################
app = Flask(__name__)

#################################################
# Database Setup
#################################################
from flask_sqlalchemy import SQLAlchemy

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql' + os.environ.get('DATABASE_URL', '')[8:]
# app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', '') or "sqlite:///db.sqlite"

# Remove tracking modifications
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

Ecom = create_classes(db)

#################################################
# Flask Setup
#################################################
app = Flask(__name__)

#################################################
# Flask Routes
#################################################

# CREATE STATIC PAGES


#Home page 
@app.route("/")
def home():
    """List static html page."""
    return render_template("index.html")


#food visulisation page
@app.route("/food-retail.html")
def food():
    """List static html page."""
    return render_template("food-retail.html")


#non-food visulisation page
@app.route("/non-food-retail.html")
def nonfood():
    """List static html page."""
    return render_template("non-food-retail.html")


#retail visulisation page
@app.route("/australian-retail-market.html")
def retail():
    """List static html page."""
    return render_template("australian-retail-market.html")


# CREATE API PAGES

@app.route("/api/v1.0/data")
def jdata():

    """Return a list of all ecommerce data frame info"""
    # Query all water data
    results = db.session.query(Ecom.date, Ecom.year, Ecom.month, Ecom.online_food_turnover, Ecom.online_nonfood_turnover, Ecom.online_total_turnover, Ecom.total_revenue_turnover).all()


    # Create a dictionary from the row data and append to a list of all_ecom
    all_ecom = []
    for date,year,month,online_food_turnover,online_nonfood_turnover,online_total_turnover,total_revenue_turnover in results:
        ecom_dict = {}
        ecom_dict["date"] = date
        ecom_dict["year"] = year
        ecom_dict["month"] = month
        ecom_dict["online_food_turnover"]=online_food_turnover
        ecom_dict["online_nonfood_turnover"]=online_nonfood_turnover
        ecom_dict["online_total_turnover"]=online_total_turnover
        ecom_dict["total_revenue_turnover"]=total_revenue_turnover
        all_ecom.append(ecom_dict)

    return jsonify({"data":all_ecom})

if __name__ == '__main__':
    app.run(debug=True)




