from re import L
from wsgiref import headers
from requests import request
from selenium import webdriver
from bs4 import BeautifulSoup
import csv

start = "https://exoplanets.nasa.gov/discovery/exoplanet-catalog/"


bro = webdriver.Chrome("chromedriver.exe")
bro.get(start)

planetdata = []
newplanetdata = []
final = []

def scrape ():
    headers = ["name", "light_years_from_earth", "planet_mass", "stellar_magnitude", "discovery_date", "hyper_link", "planet_type", "planert_radius", "orbital_period", "orbital_radius", "eccentricity"]
    for i in range(0,201):
        soup = BeautifulSoup(bro.page_source, "html.parser")
        for ul in soup.find_all("ul", attrs = {"class", "exoplanet"}):
            litags = ul.find_all("li")
            templist = []
            for index,li in enumerate(litags):
                if index == 0:
                    templist.append(li.find_all("a")[0].contents[0])
                else:
                    try:
                        templist.append(li.contents[0])
                    except:
                        templist.append("")
            hyperlinktag = litags[0]
            templist.append("https://exoplanets.nasa.gov" + hyperlinktag.find_all("a", href = True)[0]["href"])
            planetdata.append(templist)
    # with open("file.csv", "w", newline = "") as f :
    #     object = csv.writer(f)
    #     object.writerow(headers)
    #     object.writerows(planetdata)

scrape()

def scrape2 (hyperlink):
    page = request.get(hyperlink)
    soup = BeautifulSoup(page.content, "html.parser")
    templist = []
    for tr in soup.find_all("tr", attrs = {"class" : "fact_row"}):
        td = tr.find_all("td")
        for tdtag in td:
            templist.append(tdtag.find_all("div", attrs = {"class": "value"}))
    newplanetdata.append(templist)


for index,data in enumerate(planetdata):
    scrape2(data[5])
for index,data in enumerate(planetdata):
    final.append(data + newplanetdata[index])
with open ('final.csv')as f:
    object = csv.writer(f)
    object.writerow(headers)
    object.writerows()