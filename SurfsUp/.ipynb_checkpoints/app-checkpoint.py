# Import the dependencies.
import datetime as dt
import numpy as np
import pandas as pd

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify


#################################################
# Database Setup
#################################################


# reflect an existing database into a new model
engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# reflect the tables
Base = automap_base()
Base.prepare(autoload_with=engine)
Base.classes.keys()

# Save references to each table
# Measurement = Base.classes.measurement
# Stations = Base.classes.station

# Create our session (link) from Python to the DB
# session = Session(engine)

#################################################
# Flask Setup
#################################################
# app = Flask(__name__)

#################################################
# Flask Routes
#################################################
# @app.route("/")
# def home():
#     return(
#         f"Available Routes:<br/>"
#         f"/api/v1.0/precipitation<br/>"
#         f"/api/v1.0/stations<br/>"
#         f"/api/v1.0/tobs<br/>"
#         f"/api/v1.0/<start><br/>"
#         f"/api/v1.0/<start>/<end>"
#         )

# @app.route("/api/v1.0/precipitation"):
# def precipitation():
