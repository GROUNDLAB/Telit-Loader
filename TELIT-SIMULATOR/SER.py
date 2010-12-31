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


#dummy class to test compilation
import time
import sys
import threading

def send(string):
	print string
def sendbyte(byte):
	
	print "[SER] sent:" + hex(byte)
def set_speed(bitrate):
	print "[SER] setting bitrate:" + bitrate
#######################################################


#PYthON HAS NO GOOD WAY TO KILL A THREAD OR TIME PROCESS
input=""
###################################
def inputThread():
	global input
	next=""
	#timer = time.time()+timeout	
	#while time.time() < timer:
	while 1:
		#read input
		print "going:"
		#time.sleep(.1)				#can't hammer CPU
		next = sys.stdin.read(1)            	# read a one-character string
		#next = raw_input()
		if next == "\r" or next == "\n":	# or an empty string at EOF
       			break
		if not next:
			pass
		else:	
			input += next
	return input	
#####################################

def receiveiFancy(timeout):
	
	print "[SER] ###Wating:%i seconds for keyboard input:"%(timeout)
	print "[SER] Type something then press (ENTER/RETURN) to end input###"
	
	T = threading.Thread(target=inputThread)
	T.start()
	T.join(timeout)

	return input
########################################################
#use below works better


def receive(timeout):
	
	print "[SER] ###Wating:%i seconds for keyboard input:"%(timeout)
	print "[SER] Type something then press (ENTER/RETURN) to end input###"
	next=""
	input=""
	timer = time.time()+timeout	
	while 1: 
		
		#read input
		time.sleep(.1)				#can't hammer CPU
		next = sys.stdin.read(1)            	# read a one-character string
		#next = raw_input()
		if next == "\r" or next == "\n":	# or an empty string at EOF
       			break
		if not next:
			pass
		else:	
			input += next
	if time.time() > timer:
		print "[SER] Timeout occured during input." 
	return input
########################################################




