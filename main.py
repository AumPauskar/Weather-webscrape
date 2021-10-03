# weather webscrape
# importing all the modules
from bs4 import BeautifulSoup
import requests

# required url, may do json/txt in the future
source = requests.get('https://weather.com/en-IN/weather/tenday/l/Istanbul+Park+16774:25:TU').text
# grabs the html document
soup = BeautifulSoup(source, 'lxml')
# finds the temprature section from the html document
article = soup.find("span", {"class": "DailyContent--temp--3d4dn","data-testid": "TemperatureValue"})
current_temp = article.text
print(current_temp)