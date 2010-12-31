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


import time

def reactivatePython():
  # simulation impossible
  return

def secCounter():
  sec = time.time()
  return int(sec)

def sleep(tenthOfSec):
  sec = float(tenthOfSec)/10
  print "sleeping ",sec,"sec"
  time.sleep(sec)
  return

def powerSaving(seconds):
  print 'dummy powerSaving(', seconds, ')'
  time.sleep(seconds)
  return

def powerSavingExitCause():
  print 'dummy powerSavingExitCause()'
  return 1

def watchdogEnable(seconds):
  print 'dummy watchdogEnable(', seconds, ')'
  return

def watchdogReset():
  print 'dummy watchdogReset()'
  return

def watchdogDisable():
  print 'dummy watchdogDisable()'
  return

