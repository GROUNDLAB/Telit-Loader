import sys,os
import optparse



#Gets file name from options##############################################
def getFile():
	parser = optparse.OptionParser()		#create and init optionParser
	parser.add_option("-f", "--file",\
		action = "store", type = "string",\
		dest = "FILE", help="py file name")
	(options, args) = parser.parse_args()		#parse options
	#errorcheck options
	if options.FILE is None:
		print "You must specify a file EG. make upload FILE=myFile.py"
	else:
		 print options.FILE		


##########################################################################

getFile()


