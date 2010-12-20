import GPS
import SER
import MDM
import MOD


#gets reply###works###############################################################
def getReply():
	reply = MDM.receive(20)
	if reply.find("OK"):
		return reply
	SER.send(reply)		#if it was bad send out reply for debug and NULL
	return 0
###############################################################################

#init###works#################################################################
def init():
	#AT+CMGF=1 set text mode not PDU
	MDM.send('ATE0\r',0)
	reply = getReply()
	SER.send(reply)
	MDM.send('AT+CMGF=1\r', 0)
	reply= getReply()
	SER.send(reply)
##########################################################################
	
#CSQ###works####################################################################
def getCSQ():
	#<CR><LF>OK<CR><LF>
	#Get signal strength. +CSQ: <rssi (more=better)>, <ber, less=better>	
	MDM.send('AT+csq\r', 0)
	CSQ = MDM.receive(30)
	if CSQ.find("OK"):
		formatedCSQ = CSQ.split("\r\n")[1].replace("+CSQ:","").\
		replace(" ","").split( ",")[0]
		return formatedCSQ 
	SER.send(GPS)
	return 'ERROR'
	#to turn it into a int do int(CSQ)
############################################################################################

#BAT###works################################################################################
def getBAT():
	MDM.send('AT#CBC\r', 0)
	BAT = MDM.receive(20)
	if BAT.find("OK"):
		formatedBAT = BAT.split("\r\n")[1].replace("#CBC:","").split( ",")[1]
		return formatedBAT
	SER.send(GPS)
	return 'ERROR'
############################################################################################

#GPSAI###work###checks gps current##########################################################
#$GPSAI:<value>[,<status>]
def getGPSAMP():
	MDM.send('AT$GPSAI\r', 0)
	GPS = MDM.receive(20)
	if GPS.find("OK"):
		formatedGPS = GPS.split("\r\n")[1].replace("$GPSAI:","").split( ",")[0]
		return formatedGPS
	SER.send(GPS)
	return 'ERROR'
############################################################################################

#GPSACP###work###gets last position#########################################################
#$GPSACP: <UTC>,<latitude>,<longitude>,<hdop>,<altitude>,
#<fix>,<cog>,<spkm>,<spkn>,<date>,<nsat>
def getGPS():	
	MDM.send('AT$GPSACP\r', 0)
	GPS = MDM.receive(20)
	if GPS.find("OK"):
		formatedGPS = GPS.split("\r\n")[1].replace("$GPSACP:" , "")
		return formatedGPS
	SER.send(GPS)
	return 'ERROR'
############################################################################################

#works###########################################################################################
#AT+CMGS //sends SMS without storing
def sendNoSaveCMGS(theNumber, theMessage):
#RETURNS > 
        MDM.send("AT+CMGS=\"",1)
        MDM.send(theNumber,1)
        MDM.send("\"\r",1)
	PROMT= MDM.receive(25)
	print PROMT
        if '>' in PROMT:
       		MDM.send(theMessage,0)
        	MDM.sendbyte(0x1A,0)				#CTR-Z finishes text
		REPLY = MDM.receive(100)
		if REPLY.find("OK"):
        		return 'OK'                     	# good send
        	else:
			return REPLY
	else:
		MDM.sendbyte(0x1B,0);				#kills the send
		return "ERROR";        				# if we got here it failed
#############################################################################################

#sendSMS##WORKS##### with checking CSQ#######################################################
def checkSend(_NUMBER, _MESSAGE):
	CSQ = getCSQ()
	SER.send(CSQ)
	intCSQ = int(CSQ)	#convert to int 
	if intCSQ != 99:	#99 is no signal
		if intCSQ > 1:	#if it is a good quality
			reply = sendNoSaveCMGS(_NUMBER, _MESSAGE) #send
			return reply
	return "no send"
##############################################################################################

#makes SMS message##Works#####################################################################
def makeSendMes():
	BAT = getBAT()
	CSQ = getCSQ()
	pos=GPS.getActualPosition()
	modID="kali"	
	fullData = "LION "+ modID + "," + ",".join([pos ,CSQ ,BAT])
	SER.send(fullData)
	return fullData
##############################################################################################

##################################
SER.set_speed('9600')
SER.send('hello world!\n')
SER.send('initing!')
init()
	
for i in range(3):
#while 1:
	SER.send('Getting APN OPTIONS')
	#Short code "47647" LION

	#SER.send('sending firts message')	
	NUMBER = "47647"
	MESSAGE = makeSendMes()	
	reply = checkSend(NUMBER, MESSAGE)
	SER.send(reply)
	SER.send('out of send message')
	MOD.sleep(10)

#	SER.send('sending second message')
#	NUMBER = "3473017780"
#	MESSAGE = makeSendMes()	
#	checkSend(NUMBER, MESSAGE)
#	MOD.sleep(10)

#	BAT = getBAT()
#	SER.send(BAT)
#	CSQ = getCSQ()
#	SER.send(CSQ)
#	GPSA = getGPSAMP()
#	SER.send(GPSA)
#	GPS = getGPS()
#	SER.send(GPS)	
#	getAPNSettings()
	#SER.send('running options\n')
	#optionMenu()	
SER.send("check out")
DEATHTOPROGRAM()
#################################################################################
#END
#################################################################################
