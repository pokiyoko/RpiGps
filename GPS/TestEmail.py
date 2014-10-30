import signal 													# Import Signals
import sys
import smtplib

limit = 90

user = "testinghardware61@gmail.com"
print "u = {}".format(user)

psd = "jijiharon"
print "p = {}".format(psd)

maillist = ['vcamargo.e@gmail.com']
topic = "Email Test!"
Text = "Hello World!\n Test {} \n Test {}".format(0.0,0.0)



def sendMail(sender = user , psw = psd, toRecipe = maillist, sub = topic, Info = Text ):
	gmail_user = sender
	gmail_pwd = psw

	FROM = sender
	TO = toRecipe
	SUBJECT = sub
	TEXT = Info

	            # Prepare actual message
	message = """\From: %s\nTo: %s\nSubject: %s\n\n%s""" % (FROM, ", ".join(TO), SUBJECT, TEXT)

	#server = smtplib.SMTP(SERVER) 
	server = smtplib.SMTP("smtp.gmail.com", 587) #or port 465 doesn't seem to work!
	server.ehlo()
	server.starttls()
	server.login(gmail_user, gmail_pwd)
	server.sendmail(FROM, TO, message)
	#server.quit()
	server.close()
	print 'successfully sent the mail'


sendMail()