#AVR SOURCE FILES FOR GSM,SERIAL FUNCTIONALITY###########################
# 	                                                   		#
#                    Copyright (C) 2010  Justin Downs of GRounND LAB	#
#                    www.GroundLab.cc  			1%      	#
#                     							#
#					Code based off:			#
#		      			Josh Levinger  			#
#			http://jlev.media.mit.edu/Projects/GeoTracker 	#
#					Further modified by:		#
#					Lucas Vickars	                #
# This program is free software: you can redistribute it and/or modify 	#
# it under the terms of the GNU General Public License as published by 	#
# the Free Software Foundation, either version 3 of the License, or    	#
# at your option) any later version.                                   	#
#                                                                      	#
# This program is distributed in the hope that it will be useful,      	#
# but WITHOUT ANY WARRANTY; without even the implied warranty of       	#
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the        	#
# GNU General Public License for more details.                         	#
#                                                                      	#
# You should have received a copy of the GNU General Public License    	#
# with this program.  If not, see <http://www.gnu.org/licenses/>.      	# 
#########################################################################


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
		print "OPENING SERIAL CONNECTION#######\nPort: " + PORT + "\n" "Baud: " + BAUD 
		print "################################"
###########################################################################	

#gets reply#################################################################
def getReply(timeSleep=.1):
##THERE IS A BUG IN HERE FOR LARGE AMOUNTS OF DAtA FIX LATER!!!!!
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
		print "Telit replied, communications OK....."
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


