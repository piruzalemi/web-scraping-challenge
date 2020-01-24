# Web-scraping-challenge
------------------------

# Part 1 - Scraped using Jupyter Notebook, BeautifulSoup, Pandas, and Requests/Splinter + Flask

  The following explains what i scraped:

 # NASA Mars News

 1. Scraped the NASA Mars News Site and collected the latest News Title and Paragraph Text.
 2. Assigned the text to variables so that I could reference later: See:
 https://mars.nasa.gov/news/page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest

Example:
news_title = "NASA's Next Mars Mission to Investigate Interior of Red Planet"
news_p = "Preparation of NASA's next spacecraft to Mars, InSight, has ramped up this summer, on course for launch next May from Vandenberg Air Force Base in central California -- the first interplanetary launch in history from America's West Coast."

# JPL Mars Space Images
  3. Visited the url for JPL Featured Space. https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars
  4. Used splinter to navigate the site and found the image url for the current Featured Mars Image and 
  5. Assigned the url string to a variable called featured_image_url.
  6. Made sure to find the image url to the full size .jpg image.
  7. Made sure to save a complete url string for this image.
    Example:
    featured_image_url = 'https://www.jpl.nasa.gov/spaceimages/images/largesize/PIA16225_hires.jpg'
    
# Mars Weather:

  8. Visited the Mars Weather twitter account and 
  9. Scraped the latest Mars weather tweet from the page. 
  10 Saved the tweet text for the weather report as a variable called mars_weather.
    # Example:
    mars_weather = 'Sol 1801 (Aug 30, 2017), Sunny, high -21C/-5F, low -80C/-112F, pressure at 8.82 hPa, daylight 06:09-17:55'
    
 # Mars Facts

  11. Visited the Mars Facts webpage https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest
  and used Pandas to scrape the table containing facts about the planet including Diameter, Mass, etc.
  12. Used Pandas to convert the data to a HTML table string.
  
# Mars Hemispheres

  13. Visited the USGS Astrogeology site here to obtain high resolution images for each of Mar's hemispheres.
  14. Clicked each of the links to the hemispheres in order to find the image url to the full resolution image.
  15. Saved both the image url string for the full resolution hemisphere image, and the Hemisphere title containing 
      the hemisphere named. 
  16. Used a Python dictionary to store the data using the keys img_url and title.
  17. Appended the dictionary with the image url string and the hemisphere title to a list. 
      This list contained one dictionary for each hemisphere.
      
      I saved all the interesting information in MongoDB

----------------------------------------------------------------------------------------------------------
#-                     Part 2 - Mongo DB  with Flask Templating + Applications                           -
----------------------------------------------------------------------------------------------------------

In Part2 : Used MongoDB with Flask templating to create a new HTML page that displayed all of the information 
that was scraped from  a set of URLs 

    a. Converted my Jupyter notebook into a Python script called scrape_mars.py with a function called scrape that 
    executed all of my scraping code from above and returned one Python dictionary containing all of the scraped data.
    
    b. Created a template HTML file called index.html that took the mars data dictionary and displayed all of the 
    data in the appropriate HTML elements. 
    
Note: To achieve the above efficiently - a. I Used Splinter to navigate the sites when needed and 
                                         b.  BeautifulSoup to help find and parse out the necessary data.



# Making it easier:

I Used Pymongo for CRUD applications for my database. To maintain simplicity, I overwrote the existing document each time the /scrape url is visited and new data is obtained.

I used Bootstrap to structure my HTML template. Thats smart! as it saved me time.

The Jupyter Notebook containing the scraping code used, is in this depository under 3 days! + screen shots of my final application. Thats a record time of production

Enjoy! Health & Happiness. Piruz Alemi Jan 24, 2020.
