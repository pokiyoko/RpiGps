from serial import Serial
import pynmea2

GPS = Serial(port = '/dev/ttyUSB0', baudrate = 4800)
GPS.flush()

for i in range(10):
	inp_data = GPS.readline()
	msg = pynmea2.parse(inp_data)
	print msg
	try:
		print msg.timestamp
		print "Longitude: {}".format(msg.longitude)
		print "Latitude: {}".format(msg.latitude)
		print "Speed: {}".format(msg.spd_over_grnd)
		print msg
	except:
		pass
	