import serial
import sys
import time

#gets Serial prt settings from settings.txt################################
global PORT 
PORT = None
global BAUD 
BAUD = None	
global telitPort 
telitPort = None
def getSerialSettings():
	global PORT
	global BAUD
	with open("settings.txt") as f: #using with you don't have to call close()
	    for line in f:
	        args=line.replace('\n','').split(" ")
		if args[0].lower() == "port":
			PORT = args[1]
		elif args[0].lower() == "baud":
			BAUD = args[1]
		else:
			 pass
	
	if PORT==None or BAUD==None:
		print "****ERROR BAD SYNTAX -> Check \"settings.txt\" file \n\
	Syntax is:\n PORT(space)/dev/myportblah.tty(RETURN)\
	\n BAUD(space)9600(RETURN)"
	
	else:
		print "USING##############\nPort: " + PORT + "\n" "Baud: " + BAUD 
###########################################################################	

#checks for Telit with a AT#################################################
def heartBeat():
	global telitPort
	telitPort.flushInput() #clear buffer of junk
	telitPort.write("AT\r") #send a AT<CR>
	time.sleep(1)
	input = telitPort.readlines()
	
	if "OK\r\n" not in input:
		print "Failed to talk to Telit is it on? is the RX TX right?"
		print "Try to figure it out and try again"
		sys.exit(1)
	else:
		print "we said hello"
		return True
##############################################################################

#OPENS SERIAL PORT############################################################
def openSerial():
	global telitPort
	try:
		telitPort = serial.Serial(PORT,BAUD,timeout=1,bytesize=8,\
		stopbits=1,parity='N',writeTimeout=1)
		telitPort.open()
	except serial.SerialException,e:
		print "SERIAL FAILURE: ",e
		print "CHECK settings.txt file"
		sys.exit(1) #bad for UNIX
	if heartBeat():
		return True
###############################################################################		 

#OPEN SOCKET CHECK FOR TELIT###################################################
def serialOpenCheck():
	getSerialSettings()
	openSerial()
	return True
###############################################################################

#close Socket##################################################################
def serialClose():
	telitPort.close()
###############################################################################

serialOpenCheck()
serialClose()


