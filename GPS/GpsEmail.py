from serial import Serial
import pynmea2
import smtplib
import datetime

import signal 													# Import Signals
import sys

limit = 90

user = "testinghardware61@gmail.com"
psd = "jijiharon"
maillist = ['vcamargo.e@gmail.com','zulfikri1980@gmail.com']
topic = "Speed Warning!"
Text = ""


class SpeedCheck():
	def __init__(self,port = '/dev/ttyUSB0' ,limit = 90):
		self.__port = Serial(port)
		self.__port.baudrate = 4800
		self.limit = limit
		self.speed = 0
		self.latitude = 0
		self.longitude = 0
		self.warning = False

	def check():
		inp_data = self.__port.readline()
		try:
			msg = pynmea2.parse(inp_data)
		except:
			pass
		try:
			self.__longitude = msg.longitude
			self.__latitude = msg.latitude
			self.__speed = msg.spd_over_grnd * 1.852

			return True
		except:
			return False

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

while 1:
	if Sensor.SpeedCheck():
		if Sensor.speed >= Sensor.limit and Sensor.warning == False:
			Sensor.warning = True

			Text = "Your car WWD2025 exceeding 90km per hour in this location: \n latitude: {}\n longitude: {}".format(Sensor.longitude,Sensor.latitude)

			sendMail()

		if Sensor.speed <= Sensor.limit - 30 and Sensor.warning:
			Sensor.warning = False

	signal.signal(signal.SIGINT, signalHandler)


def signalHandler(signal, frame):
    print 'You pressed Ctrl+C!'
    sys.exit(0)

#sendMail()