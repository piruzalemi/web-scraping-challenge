from splinter import Browser
from bs4 import BeautifulSoup as bs
import time


def init_browser():
    # ---------------------------------------------------------------------
    # @NOTE: Replace the path with your actual path to the chromedriver
    # executable_path = {"executable_path": "/usr/local/bin/chromedriver"}
    #                                            Piruz Alemi Jan 27, 2020
    # ---------------------------------------------------------------------
    executable_path = {"executable_path": "./bin/chromedriver"}
    return Browser("chrome", **executable_path, headless=False)


def scrape_info():
    browser = init_browser()

    # ------------------------------------------------------------------
    #        Use Splinter to initiate a "visit" to the browser!
    #        And freeze it for 2 seconds!
    #        Use html parser for Soup of this visit
    # -----------------------------------------------------------------
    # Visit visitcostarica.herokuapp.com
    # Visit: https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars
    # url = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
    url = "https://www.jpl.nasa.gov"
    browser.visit(url)

    time.sleep(2)

    # Scrape page into Soup
    html = browser.html
    soup = bs(html, "html.parser")
    print(soup)
    # ------------------------------------------------------------------------
    # Get the the videos with mp4 type
    # avg_temps = soup.find('div', id='weather')
    # <source src='/images/exoplanet/20200124/PIA21472.m4v' type='video/mp4'>
    # The code for video was extracted after "inspecting" the website
    # ------------------------------------------------------------------------
    # video = soup.find('source', type='video/mp4')
    paragraph = soup.find('<p>')
    # Get the min avg temp
    # min_temp = avg_temps.find_all('strong')[0].text
    title = soup.title.string

    title_content=soup.title.contents[0]
    paragraph_content=soup.p.contents[0]

    # ------------------------------------------------------
    #      How to load a list of href  into the dictionary?
    #      Gets all href
    # -----------------------------------------------------
    for link in soup.find_all('a'):
        links=link.get('href')
    # ------------------------------------------------------
    #       Gets all the texts
    # ------------------------------------------------------
    text=soup.get_text()
    # Get the max avg temp
    # max_temp = avg_temps.find_all('strong')[1].text
    
    # BONUS! : Find the src for nasa images
    relative_image_path = soup.find_all('img')[2]["src"]
    # nasa_img = url + relative_image_path
    nasa_img = relative_image_path

    # Store data in a nasa dictionary
    nasa_data = {
        "nasa_img": nasa_img,
        "Title": title_content,
        "Text": text,
        "Links": links,
        "paragraph": paragraph_content

    }

    # Close the browser after scraping
    browser.quit()

    # Return results 
    return nasa_data
