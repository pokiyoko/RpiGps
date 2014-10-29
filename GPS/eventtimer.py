from datetime import datetime
from datetime import timedelta

class EventTimer(object):

	def __init__(self, hours = 0, minutes = 0, seconds = 0):
		self.__delta = timedelta(hours = hours, minutes = minutes, seconds = seconds)

	def run(self):
		self.__inTimer = datetime.now()

	def ready(self):
		chk_time = datetime.now()
		if chk_time - self.__inTimer >= self.__delta:
			self.__inTimer = datetime.now()
			return True
		else:
			return False

class RunControl(object):
	def __init__(self):
		self.__ini = 0
		self.__end = 0
		self.__status = False
		self.__change = False

	def setInit(self,hours = 0, minutes = 0):
		self.__ini = datetime(2014,1,1,hours,minutes,0,0)

	def setEnd(self,hours = 0, minutes = 0):
		self.__end = datetime(2014,1,1,hours,minutes,0,0)

	def status(self):
		now = datetime.now()
		if not self.__status:
			if self.__ini.hour < now.hour:
				
				self.__status = True
				self.__change = True

			if self.__ini.hour == now.hour:
				if self.__ini.minute <= now.minute:

					self.__status = True
					self.__change = True

		if self.__status:
			if self.__end.hour < now.hour:
				
				self.__status = False
				self.__change = True

			if self.__end.hour == now.hour:
				if self.__end.minute <= now.minute:
					self.__status = False
					self.__change = True

		return self.__status

	def firstTime(self):
		if self.__change:
			self.__change = False
			return True
		else:
			return False