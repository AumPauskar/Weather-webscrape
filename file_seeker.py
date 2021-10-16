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

def GetMailStatus():
	import json
	with open ('config.json') as file:
		data = json.load(file)
		return (data['mail-tag'])

def GetSenderMail():
	import json
	with open('mail_list.json') as file:
		data = json.load(file)
		sender = (data['sender'])[0]
		email_address = (sender['email'])
		email_password = (sender['password'])
		sender_credentials = [email_address, email_password]
		return sender_credentials

def GetReceiverMail():
	import json
	arr = []
	with open('mail_list.json') as file:
		data = json.load(file)
		receiver = data['receiver']
		for a in range(0, len(receiver)):
			recipient = receiver[a]
			arr.append(recipient['email'])
		return arr