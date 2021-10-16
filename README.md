# Weather-webscrape
## Modules involved
* Modules used
	1. BeautifulSoup4
	> pip install beautifulsoup4
	2. HTML5LIB
	> pip install html5lib
	3. smtplib
	> pip install secure-smtplib
	4. OS
	preinstalled
	
* Settings involved in sending mail
Please use two-factor authentication before doing anything with python mailing for extra security or use a dummy account for sending mail. Go to the following link for seeing how to give access to python also app passwords can be used if you are using two-factor authentication.
> myaccount.google.com/lesssecureapps


* Important changes to do before using the program
For the program to work the user must change a few lines of code. Don't worry its not that complicated you have to only change a couple of lines of code and after that you are set to use the code.
	1. Enviorment variables
	To maintain security of your email address and password we have used enviorment variables to store both the email address and password in the environment variables. To do this please open the environment variable settings and then assign a key tmail-->mail id and tpwd-->mail password. If you don't want to do it then you can: 
		- Open config.json and change mail-tag to False (with capital F) 
		- Open mail_list.json and under the sender tag enter email and password in the given space
	2. Input weather location
	To enter the weather location, google search the location you require and click the link where it is hosted by weather.com and under the 10 day weather data. Now when you get the link be sure to put the link inside the file_seeker program under weather-tag.
	3. Recipients
	The file stores the input of n number if recipients. To put the recipients data inside the program you include the name and email address under receiever dictionary. Now put the name and email address in front of the corresponding the tags, and if you want more people to send, then you can just copy paste the code snippet and you can just rinse and repeat.