def GetLocation():
	import json
	with open('config.json') as file:
		data = json.load(file)
		return(data['weather-tag'])

def GetSubject():
	import json
	with open('config.json') as file:
		data = json.load(file)
		return(data['subject-tag'])

def GetMessage():
	import json
	with open('config.json') as file:
		data = json.load(file)
		return(data['message-tag'])

def GetRecieverMail():
	import json
	with open('mail_list.json') as file:
		data = json.load(file)
		