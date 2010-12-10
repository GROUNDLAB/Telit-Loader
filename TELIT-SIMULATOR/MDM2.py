#simulation class, talks to EVK
import serial, time
global port

def setup(portname):
	global port
	port = serial.Serial(portname,115200,timeout=1,bytesize=8,stopbits=1,parity='N',writeTimeout=1)
	port.open()

def send(string, timeout):
	global port
	port.write(string) #pyserial doesn't have a timeout
	print "[send]:",string


def receive(timeoutTenthOfSec):
	global port
	port.flushInput() #necessary?
	sec = int((timeoutTenthOfSec+5)/10)
	time.sleep(sec)
	resp = port.readlines()
	string = ''.join(resp)
	#print "[recv]:",string
	return string

