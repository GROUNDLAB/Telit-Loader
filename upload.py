import sys,os
import optparse


global fileInput
#Gets file name from options##############################################
def getFile():
	global fileInput
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
		print "Opening:" options.FILE		
		file = open(options.FILE,'r')
		fileInput = file.readlines()
		scriptLength = os.path.getsize(options.FILE)
		######***TO COMPENSATE FOR FILE SIZE BUG***########
		scriptLength += scriptLength + 20
##########################################################################

getFile()


