def SendMail(mail_report, subject):

	import smtplib
	import os
	import file_seeker

	mail_status = file_seeker.GetMailStatus()
	if mail_status == "True":
		sender_mail = os.environ.get('tmail')
		sender_pswd = os.environ.get('tpwd')
	elif mail_status == "False":
		temp = file_seeker.GetSenderMail()
		sender_mail = temp[0]
		sender_pswd = temp[1]
	else:
		print("Enter 'True' or 'False' in the same caps")
		
	mail_list = file_seeker.GetReceiverMail()
	for a in range(0, len(mail_list)):
		reciever_mail = mail_list[a]
		with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
			smtp.ehlo()
			smtp.starttls()
			smtp.ehlo()
			smtp.login(sender_mail, sender_pswd)

			subject = subject
			body = mail_report

			msg = f'Subject: {subject}\n\n{body}'

			smtp.sendmail(sender_mail, reciever_mail, msg)
