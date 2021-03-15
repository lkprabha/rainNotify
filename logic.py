
from selenium import webdriver
from bs4 import BeautifulSoup
import requests

#browser = webdriver.Chrome()
#browser.get("https://www.accuweather.com/en/sg/singapore/300597/daily-weather-forecast/300597")

##$x("//div[@class='right']/p[@class='panel-item']/span[@class='value']")[1].textContent

url = "https://www.accuweather.com/en/sg/singapore/300597/daily-weather-forecast/300597"
r = requests.get(url)
data = r.text
soup = BeautifulSoup(data, "html.parser")
spanTxt=soup.find("p",
span = soup.find("p", class="panel-item")
print(span.text)
