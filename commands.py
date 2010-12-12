import sys,os
import optparse
import setPort
import time

global fileInput
global fileLength
global fileName
#Gets file name from options##############################################
def getFile():
	global fileInput
	global fileLength
	global fileName
	parser = optparse.OptionParser()		#create and init optionParser
	parser.add_option("-f", "--file",\
		action = "store", type = "string",\
		dest = "FILE", help="py file name")
	(options, args) = parser.parse_args()		#parse options
	#errorcheck options
	if options.FILE is None:
		print "You must specify a file EG. make upload FILE=myFile.py"
		sys.exit(1) #bad for UNIX
	else:
		fileName = options.FILE			#the name of the file
		print "Opening:"+ fileName		
		file = open(fileName,'r')
		fileInput = file.readlines()
		fileLength = os.path.getsize(fileName)
		######***TO COMPENSATE FOR FILE SIZE BUG***########
		fileLength += 20
##########################################################################

#Sends File###############################################################
def writeFile():
	global fileInput
	global fileLength
	global fileName
	global telitPort
	
	print "writing file:"
	print fileName
	print fileLength
		
	writeCommand= "AT#WSCRIPT=%s,%i\r\n" % (fileName,fileLength)
	print "Sending:" + writeCommand
	setPort.serialOpenCheck()			#open serial connection send AT to check
	setPort.telitPort.flushInput()			#get rid of junk
	setPort.telitPort.write(writeCommand)
	input = setPort.getReply()			#from setPort
	if ">>>" not in input:
		print "didn't get >>>??"
		print input		
		sys.exit(1)
	print"START FILE#########"
	lineMarker=0
	for line in fileInput:
		try:	#two from back is /n/l
			if(line[-2:] == "\r\n"):
				writeLine=line
			#it is somthing else post append \r\n
			else:
				writeLine=line + "\r\n"
			#write out to port
			setPort.telitPort.write(writeLine)
			#print what we wrote
			print "%i: %s" % (lineMarker,writeLine)
			lineMarker+=1
			time.sleep(.1) #sleep a bit to see the line
		except setPort.serial.serialutil.SerialTimeoutException:
			print "serial timed out on line " + lineMarker	
			setPort.serialClose()
			sys.exit(1)
	setPort.telitPort.flush()
	print"END FILE###########"


#test			
getFile()
writeFile()
#print fileLength
#print fileInput

