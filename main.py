from bs4 import BeautifulSoup
import requests

def scrape(url):
    r = requests.get(url)
    return r.text


movieName = input("Enter movie/TV name   :   ")

urlDir = "https://www.google.co.in/search?q="+movieName+"+director"
print(urlDir)

html = scrape(urlDir)
soup = BeautifulSoup(html, "html.parser")
#director = 

#print(soup.prettify())
dirString = (soup.findAll("div", {"class": "BNeawe s3v9rd AP7Wnd"}))[0]
print(dirString.text.partition("is")[0])