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


#simulation class, talks to EVK
import serial, time
global port

def setup(portname):
	global port
	port = serial.Serial(portname,115200,timeout=1,bytesize=8,stopbits=1,parity='N',writeTimeout=1)
	port.open()

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

