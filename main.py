# weather webscrape
# importing all the modules
from bs4 import BeautifulSoup
import requests
import mailing
import file_seeker

# dependances
temp = ''
url = file_seeker.GetLocation()
mail_report = file_seeker.GetMessage()
subject = file_seeker.GetSubject()


# required url, may do json/txt in the future
source = requests.get(url).text
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
mail_report += temp + '.'
mailing.SendMail(mail_report, subject)
print('Message sent')