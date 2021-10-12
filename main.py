# weather webscrape
# importing all the modules
from bs4 import BeautifulSoup
import requests
import mailing

# dependances
temp = ''

# required url, may do json/txt in the future
source = requests.get('https://weather.com/en-IN/weather/tenday/l/Istanbul+Park+16774:25:TU').text
# grabs the html document
soup = BeautifulSoup(source, 'lxml')

# finds the temprature section from the html document
temprature_val = soup.find("span", {"class": "DailyContent--temp--3d4dn","data-testid": "TemperatureValue"})
current_temp = temprature_val.text
weather_status = soup.find("p", {"class": "DailyContent--narrative--hplRl", "data-testid": "wxPhrase"})
weather_report = weather_status.text
status = current_temp + '.' + weather_report

for a in range(len(status)-1):
	if status[a] == chr(176):
		pass
	elif status[a] == chr(186):
		pass
	else:
		temp += status[a]


# compiles the message in the script
mail_report = 'Hello viewer the current F1 season is looking like a great treat, especially '
mail_report += 'here at Istambul Park Turkey. The temprature right now at the track is '
mail_report += temp + '.'
mailing.SendMail(mail_report)
print('Message sent')