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


import sout
import gpsParser
import locs
import MOD
import GPIO

#MAIN
print 'PedoTracker main'
#turn off LED
GPIO.setIOvalue(12, 0)

i = 10
while (i > 0):
	pos = gpsParser.currentPosition()
	myLat = pos["lat"]
	myLon = pos["lon"]
	print "current position: %s,%s" % (myLat, myLon)
	
	if (myLat[3] != 'X' and myLon != 'X'):
		warning = 0
		for l in locs.locs:
			name = l[0]
			theLat = l[1]
			theLon = l[2]
			#one second of longitude @ 71W: 22.8m
			#one second of latitude @ 42N: 30.8m
			if((myLat[0] == theLat[0]) and (myLon[0] == theLon[0])):
				if((myLat[1] == theLat[1]) and (myLon[1] == theLon[1])):
					if((abs(myLat[2] - theLat[2]) < 2) and (abs(myLon[2] - theLon[2]) < 2)):
						print "too close to " + name
						warning = warning+1
		if (warning != 0):
			print "Proximity Alert!"
			#blink LED
#			for(j in range(10)):
#				GPIO.setIOvalue(12, 1)
#				MOD.sleep(1)
#				GPIO.setIOvalue(12, 0)
#				MOD.sleep(1)
			#pulse motor
		else:
			print "OK"
	i = i - 1
#	MOD.sleep(50) #sleep five seconds
print "done"