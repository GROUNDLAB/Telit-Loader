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
import MOD
import GPS
#import string

def currentPosition():
	pos = {}
	res = GPS.getActualPosition()
	tmp = res.split(',')
	#tmp = string.split(res,',') #for testing on mac
	pos['time'] = tmp[0]
	pos['lat'] = parseDMS(tmp[1])
	pos['lon'] = parseDMS(tmp[2])
	pos['hdop'] = tmp[3]
	pos['alt'] = tmp[4]
	pos['fix'] = tmp[5]
	pos['cog'] = tmp[6]
	pos['spkm'] = tmp[7]
	pos['spkn'] = tmp[8]
	pos['date'] = tmp[9]
	pos['nr_sat'] = tmp[10]
	return pos

#converts string to tuple
def parseDMS(dms):
	if len(dms) < 10: #don't have a good fix
		return (0,0,0,'X')
	#dms formatted like: (D)DDMM.SSSSC
	c = dms[-1] #cardinal direction
	s = int(int(dms[-5:-1])/100) #seconds
	m = int(dms[-8:-6]) #minutes
	d = int(dms[:-8]) #degrees, either two or three long	
	return d,m,s,c
