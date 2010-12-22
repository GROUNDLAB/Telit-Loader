
import GPS
import SER
import MDM
import MOD



#READ CONFIG FILE####WORKS#####################################################
PHONENUMBER=None
APN=None
PASSWORD=None
DBNUMBER=None
BAND=None
MESSAGE=None
CSQLEVEL=None
MODID=None
def getSettings():
        global PHONENUMBER
        global APN
        global PASSWORD
	global DBNUMBER
	global BAND
	global MESSAGE
	global CSQLEVEL
	global MODID

        f = open("settings.txt")
        for line in f.readlines():
                #print line
                args=line.replace('\n','').replace(' ','').split(":")
                if args[0].lower() == "phonenumber":
                        PHONENUMBER = args[1]
                if args[0].lower() == "dbphone":
                        DBNUMBER = args[1]
		elif args[0].lower() == "apn":
                        APN = args[1]
                elif args[0].lower() == "password":
                        PASSWORD = args[1]
                elif args[0].lower() == "message":
			MESSAGE = args[1]
		elif args[0].lower() == "band":
			BAND = args[1]
		elif args[0].lower() == "csqlevel":
			CSQLEVEL = args[1]
		elif args[0].lower() == "modid":
			MODID = args[1]
		else:
                        pass
        f.close()
        #print PHONENUMBER + APN + PASSWORD
        if PHONENUMBER == None:
		SER.send( "****ERROR BAD SYNTAX : PHONENUMBER -> Check \"settingsAPN.txt\" file \n"\
                + "Syntax is:\n PHONENUMBER:1234567899(RETURN)")


	elif DBNUMBER == None:
		SER.send( "****ERROR BAD SYNTAX : DBNUMBER -> Check \"settingsAPN.txt\" file \n"\
                + "Syntax is:\n PHONENUMBER:1234567899(RETURN)")


	elif APN == None:
		SER.send( "****ERROR BAD SYNTAX : APN -> Check \"settingsAPN.txt\" file \n"\
                + "Syntax is:\n PHONENUMBER:1234567899(RETURN)")


	elif PASSWORD == None:
		SER.send( "****ERROR BAD SYNTAX : PASSWORD -> Check \"settingsAPN.txt\" file \n"\
                + "Syntax is:\n PHONENUMBER:1234567899(RETURN)")


	elif MESSAGE == None:
		SER.send( "****ERROR BAD SYNTAX -> : MESSAGE -> Check \"settingsAPN.txt\" file \n"\
                + "Syntax is:\n PHONENUMBER:1234567899(RETURN)")


	elif BAND == None :
		SER.send( "****ERROR BAD SYNTAX : BAND -> Check \"settingsAPN.txt\" file \n"\
                + "Syntax is:\n PHONENUMBER:1234567899(RETURN)")

	elif CSQLEVEL == None :
		SER.send( "****ERROR BAD SYNTAX : CSQLEVEL -> Check \"settingsAPN.txt\" file \n"\
                + "Syntax is:\n PHONENUMBER:1234567899(RETURN)")
	
	elif MODID == None :
		SER.send( "****ERROR BAD SYNTAX : MODID -> Check \"settingsAPN.txt\" file \n"\
                + "Syntax is:\n PHONENUMBER:1234567899(RETURN)")

        else:
                SER.send( "\n\n####These are your connection settings#### \n"\
                "PHONENUMBER: " + PHONENUMBER + "\n" + \
                "APN: " + APN +"\n" +  \
                "PASSWORD: " + PASSWORD + "\n" + \
                "DBNUMBER: " + DBNUMBER + "\n" + \
                "MESSAGE: " + MESSAGE + "\n" + \
                "BAND: " + BAND + "\n"\
                "CSQLEVEL: " + CSQLEVEL + "\n"\
                "MODID: " + MODID + "\n"\
                 )

##############################################################################    
TIMEOUT = 0  #signals if the getreply timed out, start false no timeout
#gets reply###works###############################################################
def getReply(timeOut=10, numRep=5):
	global TIMEOUT
	FALSE=0
	TRUE=1
	TIMEOUT = FALSE
	for i in range(numRep):
		reply = MDM.receive(timeOut)
		if -1 != reply.find("OK"):
			SER.send("[MDM GET REPLY]: ")	
			SER.send(reply)
			return reply
		elif -1 != reply.find("ERROR"):	
			SER.send("[MDM GET REP ERROR]: ")	
			SER.send(reply)		#if it was bad send out reply for debug and NULL
			return FALSE
		else:
			pass
			SER.send("[MDM GET REP BAD]: ")	
			SER.send(reply)		#if it was bad send out reply for debug and NULL
	TIMEOUT = TRUE		
	return FALSE	#timeout
###############################################################################


#CSQ###works####################################################################
def getCSQ():
	#<CR><LF>OK<CR><LF>
	#Get signal strength. +CSQ: <rssi (more=better)>, <ber, less=better>	
	MDM.send('AT+CSQ\r', 0)
	CSQ = getReply(10) 
	if CSQ:
		formatedCSQ = CSQ.split("\r\n")[1].replace("+CSQ: ","").\
		replace(" ","").split( ",")[0]
		return formatedCSQ 
	SER.send(CSQ)
	return 0 #False
	#to turn it into a int do int(CSQ)
############################################################################################

#BAT###works################################################################################
def getBAT():
	MDM.send('AT#CBC\r', 0)
	BAT = getReply(10)
	if BAT:
		formatedBAT = BAT.split("\r\n")[1].replace("#CBC: ","").split(",")[1]
		return formatedBAT
	SER.send(BAT)
	return 0
############################################################################################

#GPSAI###work###checks gps current##########################################################
#$GPSAI:<value>[,<status>]
def getGPSAMP():
	MDM.send('AT$GPSAI\r', 0)
	GPSreply = getReply(10)
	if GPSreply:
		formatedGPS = GPSreply.split("\r\n")[1].replace("$GPSAI: ","").split( ",")[0]
		return formatedGPS
	SER.send(GPSreply)
	return 0
############################################################################################

#GPSACP###work###gets last position#########################################################
#$GPSACP: <UTC>,<latitude>,<longitude>,<hdop>,<altitude>,
#<fix>,<cog>,<spkm>,<spkn>,<date>,<nsat>
def getGPS():	
	GPSreply = GPS.getActualPosition()	
	SER.send(GPSreply)
	if GPSreply:
		return GPSreply
	SER.send(GPSreply)
	return 0

############################################################################################
def gpsStat():
	SER.send("\n hello benny, this is the STATUS OF GPS:\n")
	amps = getGPSAMP()	
	SER.send("\n MILLIAMPS GOING TO ANNTENNA:\n")
	SER.send(amps) 
	SER.send("\nIF IT WAS ZERO (0) CHECK THE ANNTENNA CONNECTION AND TRY AGAIN\n")
	gps = getGPS()
	SER.send("\nTHIS IS THE MOST CURRENT GPS READING WHERE ARE YOU?\n I AM IN A LITTLE ROOM IN QUEENS....\n")
	SER.send(gps)
	CSQresult = getCSQ()
 	SER.send("\nTHIS IS THE MOST CURRENT CSQ (cell signal)  READING: ")
	SER.send(CSQresult) 

##################################

#init###works#################################################################
def init():
	#AT+CMGF=1 set text mode not PDU
	MDM.send('ATE0\r',0)
	reply = getReply(10)
	SER.send(reply)
	MDM.send('AT+CMGF=1\r', 0)
	reply= getReply(10)
	SER.send(reply)
	getSettings()		#get all settings
##########################################################################
	

##################################
SER.set_speed('9600')
SER.send('hello world!\n')
	
for i in range(3):
#while 1:
	try:
	#	optionsMenu()
		SER.send('\ninit():  ')
		init()
		SER.send('\nGPS STATS:  ')
		getCSQ()
		SER.send('\nGPS STATS:  ')
		gpsStat()
		SER.send('\ngetBAT')
		getBAT()
	except Exception, e:
		SER.send(e)	#give error

	

SER.send("check out")
DEATHTOPROGRAM()
#################################################################################
#END
#################################################################################

