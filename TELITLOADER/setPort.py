import serial
import sys
import time
import os
import setWorkingDir

#gets Serial prt settings from settings.txt################################
global PORT 
PORT = None
global BAUD 
BAUD = None	
global telitPort 
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
		print "OPENING##############\nPort: " + PORT + "\n" "Baud: " + BAUD 
		print "###################"
###########################################################################	

#gets reply#################################################################
def getReply(timeSleep=.1):
	global telitPort
	tooLong = time.time()+10
	while telitPort.inWaiting() < 3 : 	
		time.sleep(1)			#You have to sleep you can't hammer the processor
		if time.time() > tooLong:
			ERROR="ERROR"
			return ERROR		#timeout somthing went wrong	
	else:
		time.sleep(timeSleep) #wait half second for all data
		input = telitPort.readlines()
	return input


############################################################################

#checks for Telit with a AT#################################################
def heartBeat():
	global telitPort
	telitPort.flushInput() #clear buffer of junk
	telitPort.write("AT\r") #send a AT<CR>
	input = getReply()	

	if "OK\r\n" not in input:
		print "Failed to talk to Telit, is it on? Is the port free?"
		print "Try to figure it out and try again"
		sys.exit(1)
	else:
		print "Telit replied proceding..........."
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
	global telitPort
	telitPort.close()
###############################################################################

#serialOpenCheck()
#serialClose()


