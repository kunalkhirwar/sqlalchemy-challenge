# Import the dependencies.
import datetime as dt

from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify


#################################################
# Database Setup
#################################################

engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()

# reflect the tables
Base.prepare(autoload_with = engine)

# Save references to each table
Measurement = Base.classes.measurement
Station = Base.classes.station

# Create our session (link) from Python to the DB
session = Session(engine)

#################################################
# Flask Setup
#################################################
app = Flask(__name__)

# #################################################
# # Flask Routes
# #################################################
@app.route("/")
def home():
    return(
        f"Welcome to my Climate App<br/>"
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/<start><br/>"
        f"/api/v1.0/<start>/<end>"
        )

@app.route("/api/v1.0/precipitation")
def precipitation():

    results = session.query(Measurement.date, Measurement.prcp).\
              filter(Measurement.date >= (dt.date(2017,8,23)-dt.timedelta(days=365))).all()
    
    output=[]

    for date, prcp in results:
        prcp_dict = {}
        prcp_dict['date'] = date
        prcp_dict['prcp'] = prcp
        output.append(prcp_dict)

    return jsonify(output)


@app.route("/api/v1.0/stations")
def stations():

    results = session.query(Station.station).all()
    
    output=[]

    for record in results:
        output.append(record.station)

    return jsonify(output)

@app.route("/api/v1.0/tobs")
def tobs():
    results = session.query(Measurement.date, Measurement.tobs).\
              filter(Measurement.date >= (dt.date(2017,8,23)-dt.timedelta(days=365))).\
              filter(Measurement.station=='USC00519281').all()
    
    output= []

    for date,tobs in results:
        tobs_dict = {}
        tobs_dict['date'] = date
        tobs_dict['tobs'] = tobs
        output.append(tobs_dict)

    return jsonify(output)

@app.route("/api/v1.0/<start>")
def start_date(start):

    try:
        start_date = dt.datetime.strptime(start, "%Y-%m-%d")

        results = session.query(Measurement.date, func.max(Measurement.tobs),
                                func.min(Measurement.tobs),func.avg(Measurement.tobs)).\
                                group_by(Measurement.date).\
                                filter(Measurement.date >= start_date - dt.timedelta(days=1)).all()
        
        output = []
        for date, TMAX , TMIN, TAVG in results:
            start_date_dict = {}
            start_date_dict['date'] = date
            start_date_dict['TMAX '] = TMAX 
            start_date_dict['TMIN'] = TMIN
            start_date_dict['TAVG'] = TAVG
            output.append(start_date_dict)

        return jsonify(output)

    except ValueError:
        return jsonify({"error": "Invalid date format. Please use YYYY-MM-DD."}), 400



@app.route("/api/v1.0/<start>/<end>")
def start_end_date(start, end):

    try:
        start_date = dt.datetime.strptime(start, "%Y-%m-%d")
        end_date = dt.datetime.strptime(end, "%Y-%m-%d")

        results = session.query(Measurement.date, func.max(Measurement.tobs),
                                func.min(Measurement.tobs),func.avg(Measurement.tobs)).\
                                group_by(Measurement.date).\
                                filter(Measurement.date.between(start_date - dt.timedelta(days=1), end_date)).all()
        
        output = []
        for date, TMAX , TMIN, TAVG in results:
            start_end_date_dict = {}
            start_end_date_dict['date'] = date
            start_end_date_dict['TMAX '] = TMAX 
            start_end_date_dict['TMIN'] = TMIN
            start_end_date_dict['TAVG'] = TAVG
            output.append(start_end_date_dict)

        return jsonify(output)
    
    except ValueError:
        return jsonify({"error": "Invalid date format. Please use YYYY-MM-DD."}), 400


if __name__ == "__main__":
    app.run(debug=True)