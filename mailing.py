def SendMail(mail_report):

	import smtplib
	import os

	sender_mail = os.environ.get('tmail')
	sender_pswd = os.environ.get('tpwd')
	reciever_mail = 'aumpauskar111@gmail.com'
	with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
		smtp.ehlo()
		smtp.starttls()
		smtp.ehlo()
		smtp.login(sender_mail, sender_pswd)

		subject = 'Weather at istambul park, Turkey'
		body = mail_report

		msg = f'Subject: {subject}\n\n{body}'

		smtp.sendmail(sender_mail, reciever_mail, msg)
		