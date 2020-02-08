
from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
#import scrape_costa
import scrape_nasa

# Create an instance of Flask
app = Flask(__name__)

# Use PyMongo to establish Mongo connection
#mongo = PyMongo(app, uri="mongodb://localhost:27017/weather_app")
mongo = PyMongo(app, uri="mongodb://localhost:27017/Nasa")
# client.list_database_names()


# Route to render index.html template using data from Mongo
@app.route("/")
def home():

    # Find one record of data from the mongo database
    # destination_data = mongo.db.collection.find_one()
    destination_data = mongo.db.news.find_one()

    # Return template and data
    return render_template("index.html", news_db=destination_data)


# Route that will trigger the scrape function
@app.route("/scrape")
def scrape():
    """
    #-----------------------------------------------------------------------------
    #
    # App.py is run under Flask. The interface between APP.py and Internet.
    # A buttom is on the index.html file, which routes the html to "/scrape"
    # We can run the "/scrape route" manually entering in a url or via a click:
    #       
    #          1. A function is stored in a program called scrape_nasa.py
    #          2. scrape_nasa.py has a function embedded in it as scrape_info
    #          3. Scrape_info is completed using Splinter + Soup for scraping
    #          4. Scrape function returns a Dictionary of key variables of interest
    #             as a dictionary called nasa_data:
    #          5. nasa_data, then gets upserted in MongoDB called Nasa.news
    #          6. Nasa database was define by Piruz Alemi, in Mongo DB to contain
    #             collections of data. These collections could also be called like
    #             Nasa.collection, or Nasa.NewsGroup or Nasa.news, etc. We can have 
    #             different collections of data under a single mongo database
    #          7. Scraped data is stored in MongoDB was via command mongo.db.collection...
    #             This part is coded in scrape_nasa.py, when we scrape using splinter
    #             + soup we also save the scrape in MongoDB 
    #          8. Control is then passed or redirected back to where we started
    #
    #                                      Piruz Alemi Jan 27th, 2020
    # ----------------------------------------------------------------------------------   
    #  Watch out! Following command, is a function called from within a program!!!! 
    # ----------------------------------------------------------------------------------            
    """
    nasa_data = scrape_nasa.scrape_info()
    # --------------------------------------------------------------------------------------
    # Update the Mongo database using update and upsert=True
    # {} are filtering parameters, 
    # nasa_data is a dictionary
    mongo.db.news.update({}, nasa_data, upsert=True)
    # mongo.db.news.insert({}, nasa_data)
    # ------------------------------------------------------------------------------------------
    # We can run mongo shell without any command-line 
    # options to connect to a MongoDB instance running on our localhost with default port 27017:
    # -------------------------------------------------------------------------------------------

    # Redirect back to home page
    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)
