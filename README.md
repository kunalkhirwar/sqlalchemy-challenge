**Introduction**
I've decided to treat myself to a long holiday vacation in Honolulu, Hawaii. To help with my trip planning, I decided to do a climate analysis about the area. The following sections outline the steps that I needed to take to accomplish this task.

**Part 1: Analyze and Explore the Climate Data**
In this section, I used Python and SQLAlchemy to do a basic climate analysis and data exploration of my climate database. Specifically, I used SQLAlchemy ORM queries, Pandas, and Matplotlib. To do so, I completed the following steps:
  
 1. Used the SQLAlchemy create_engine() function to connect to my SQLite database.
  
 2. Used the SQLAlchemy automap_base() function to reflect my tables into classes, and then saved references to the classes named station and measurement.
  
 3. Linked Python to the database by creating a SQLAlchemy session.
  
 4. Performed a precipitation analysis and then a station analysis by completing the steps in the following two subsections.

**Precipitation Analysis**
1. Found the most recent date in the dataset.

2. Using that date, got the previous 12 months of precipitation data by querying the previous 12 months of data.

3. Selected only the "date" and "prcp" values.

4. Loaded the query results into a Pandas DataFrame. Explicitly set the column names.

5. Sorted the DataFrame values by "date".

6. Plotted the results by using the DataFrame plot method.

7. Used Pandas to print the summary statistics for the precipitation data.

**Station Analysis**
1. Designed a query to calculate the total number of stations in the dataset.

2. Designed a query to find the most-active stations (that is, the stations that had the most rows). To do so, completed the following steps:

    -> Listed the stations and observation counts in descending order.
    -> Answered the question: which station id had the greatest number of observations?

3. Designed a query that calculates the lowest, highest, and average temperatures that filters on the most-active station id found in the previous query.

4. Designed a query to get the previous 12 months of temperature observation (TOBS) data. To do so, completed the following steps:

    -> Filtered by the station that had the greatest number of observations.

    -> Queried the previous 12 months of TOBS data for that station.

    -> Plotted the results as a histogram with bins=12. 

5. Closed my session.


**Part 2: Designed My Climate App**
Now that I’ve completed my initial analysis, I designed a Flask API based on the queries that I just developed. To do so, used Flask to create the routes as follows:

1. "/"

    -> Start at the homepage.
    
    -> Lists all the available routes.

2. "/api/v1.0/precipitation"

    -> Converts the query results from my precipitation analysis (i.e. retrieved only the last 12 months of data) to a dictionary using date as the key and prcp as the value.
    
    -> Returns the JSON representation of my dictionary.

3. "/api/v1.0/stations"

    -> Returns a JSON list of stations from the dataset.

4. "/api/v1.0/tobs"

    -> Queries the dates and temperature observations of the most-active station for the previous year of data.
    
    -> Returns a JSON list of temperature observations for the previous year.

5. "/api/v1.0/<start> and /api/v1.0/<start>/<end>"

    -> Returns a JSON list of the minimum temperature, the average temperature, and the maximum temperature for a specified start or start-end range.
    
    -> For a specified start, calculates TMIN, TAVG, and TMAX for all the dates greater than or equal to the start date.
    
    -> For a specified start date and end date, calculates TMIN, TAVG, and TMAX for the dates from the start date to the end date, inclusive.
