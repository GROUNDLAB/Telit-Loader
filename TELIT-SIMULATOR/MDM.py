#simulation class, talks to EVK
import serial, time
#import sys
#import fileinput
#sys.path.append('../TELIT-SIMULATOR')
#


global port
global PORTName
global BAUD

#gets reply#################################################################
def getReply(timeSleep=.1):
        global port
        tooLong = time.time()+10
        while port.inWaiting() < 3 :
                time.sleep(1)                   #You have to sleep you can't hammer the processor
                if time.time() > tooLong:
                        ERROR="ERROR"
                        return ERROR            #timeout somthing went wrong    
        else:
                time.sleep(timeSleep) #wait half second for all data
                input = port.readlines()
        return input


############################################################################


#checks for Telit with a AT#################################################
def heartBeat():
	global port
	port.flushInput() #clear buffer of junk
	port.write("AT\r") #send a AT<CR>
	input = getReply()

	if "OK\r\n" not in input:
		print "Failed to talk to Telit, is it on? Is the port free?"
		print "Try to figure it out and try again"
		sys.exit(1)
	else:
		print "Telit replied, communications OK....."
		return True
##############################################################################


###########################################################################
def getSerialSettings():
	global PORTName
	global BAUD
	
	with open("../TELITLOADER/settings.txt") as f: #using with you don't have to call close()
	    for line in f:
	        args=line.replace('\n','').split(" ")
		if args[0].lower() == "port":
			PORTName = args[1]
		elif args[0].lower() == "baud":
			BAUD = args[1]
		else:
			 pass
	
	if PORTName==None or BAUD==None:
		print "****ERROR BAD SYNTAX -> Check \"settings.txt\" file \n\
	Syntax is:\n PORT(space)/dev/myportblah.tty(RETURN)\
	\n BAUD(space)9600(RETURN)"
	
	else:
		print "OPENING SERIAL CONNECTION#######\nPort: " + PORTName + "\n" "Baud: " + BAUD 
		print "################################"

###########################################################################	


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

#OPEN PORT AUTOMATICALY WITH IMPORT
getSerialSettings()
port = serial.Serial(PORTName,BAUD,timeout=1,bytesize=8,stopbits=1,parity='N',writeTimeout=1)
port.open()
heartBeat()

