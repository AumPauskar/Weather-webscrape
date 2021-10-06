import smtplib
import os

sender_mail = os.get.environ('tmail')
sender_pswd = os.get.environ('tpwd')
reciever_mail = 'aumpauskar111@gmail.com'
with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
	smtp.ehlo()
	smtp.starttls()
	smtp.ehlo()
	smtp.login(sender_mail, sender_pswd)

	subject = 'Weather'
	body = '11'

	msg = f'Subject: {subject}\n\n{body}'

	smtp.sendmail(sender_mail, sender_pswd, msg)
	