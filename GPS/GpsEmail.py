from serial import Serial
import pynmea2
import smtplib
import datetime

from eventtimer import EventTimer 		

import signal 													# Import Signals
import sys

def readConfig():
	inp = open('config.dat','r')
	data = inp.read().split(',')
	data.remove('')
	return data

conf = readConfig()
user = conf[0]
psd = conf[1]
limit = int(conf[2])
maillist = conf[4:]

topic = "Speed Warning!"
Text = ""

MailTimer = EventTimer(minutes = 1)
MailTimer.run()

class SpeedCheck():
	def __init__(self,port = '/dev/ttyUSB0' ,limit = 90):
		self.__port = Serial(port)
		self.__port.baudrate = 4800
		self.limit = limit
		self.speed = 0
		self.latitude = 0
		self.longitude = 0
		self.warning = False

	def check(self):
		inp_data = self.__port.readline()
		try:
			msg = pynmea2.parse(inp_data)
		except:
			pass
		try:
			self.longitude = msg.longitude
			self.latitude = msg.latitude
			self.speed = msg.spd_over_grnd * 1.852

			return True
		except:
			return False

def signalHandler(signal, frame):
    print 'You pressed Ctrl+C!'
    sys.exit(0)

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

#Text = "Your car WWD2025 exceeding 90km per hour in this location: \n latitude: {}\n longitude: {}".format(0.0,0.0)

Sensor = SpeedCheck(limit= limit)

Text = """Hello User, The System is running from this point your Speed will be monitored.
Have a Nice day!
"""

sendMail(Info = Text)

print "Runing! Be Carefull I have one eye on your speed!"

while 1:
	if Sensor.check():
		if Sensor.speed >= Sensor.limit and Sensor.warning == False:
			Sensor.warning = True

			Text = "Your car WWD2025 exceeding 90km per hour in this location: \n latitude: {}\n longitude: {}".format(Sensor.longitude,Sensor.latitude)
			sendMail(Info = Text)

		if Sensor.speed <= Sensor.limit - 30 and Sensor.warning:
			Sensor.warning = False

	# if MailTimer.ready():
		
	# 	Text = "Your car WWD2025 exceeding 90km per hour in this location: \nlatitude: {}\nlongitude: {} \nSpeed: {}".format(Sensor.longitude,Sensor.latitude,Sensor.speed)
	# 	sendMail(Info = Text)

	signal.signal(signal.SIGINT, signalHandler)




#sendMail()