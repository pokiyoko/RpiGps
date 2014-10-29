import signal 													# Import Signals
import sys

limit = 90

user = "testinghardware61@gmail.com"
psd = "jijiharon"
maillist = ['vcamargo.e@gmail.com','zulfikri1980@gmail.com']
topic = "Email Test!"
Text = "Hello World!"


def sendMail(sender = user , psw = psd, toRecipe = maillist, sub = topic, Info = Text ):
	gmail_user = sender
	gmail_pwd = psw

	FROM = sender
	TO = toRecipe
	SUBJECT = sub
	TEXT = Info

	            # Prepare actual message
	message = """\From: %s\nTo: %s\nSubject: %s\n\n%s""" % (FROM, ", ".join(TO), SUBJECT, TEXT)
	try:
		#server = smtplib.SMTP(SERVER) 
		server = smtplib.SMTP("smtp.gmail.com", 587) #or port 465 doesn't seem to work!
		server.ehlo()
		server.starttls()
		server.login(gmail_user, gmail_pwd)
		server.sendmail(FROM, TO, message)
		#server.quit()
		server.close()
		print 'successfully sent the mail'
	except:
		print "failed to send mail"


sendMail()