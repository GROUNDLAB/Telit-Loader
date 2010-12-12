import sys,os
import optparse
from setPort import telitPort,getReply,serialOpenCheck(),serialClose()

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
	
	writeCommand= "AT#DSCRIPT=%s,%i\r\n" % (fileName,fileLength)
	print "Sending:" + writeCommand
	setPort.serialOpenCheck()
	telitPort.flushInput()			#get rid of junk
	#telitPort.write(writeCommand)
	#input = getReply()			#from setPort
	#if ">>>" not in input:
	#	print "didn't get >>>??"
	#	print input		
	#	sys.exit(1)




#test
getFile()
writeFile()
#print fileLength
#print fileInput

