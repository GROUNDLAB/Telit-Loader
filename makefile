
#AVR SOURCE FILES FOR GSM,SERIAL FUNCTIONALITY###########################
# 	                                                   		#
#                    Copyright (C) 2010  Justin Downs of GRounND LAB	#
#                    www.GroundLab.cc  			1%      	#
#                     							#
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

#MAKEFILE to load to telit


SOURCEFILESDIR=  $(wildcard UploadCode/*.*) 	#grab files$ (wildcard UploadCode/*.py) for just py files
SOURCEFILES= $(notdir $(SOURCEFILESDIR))	#strip directory
#checks if FILE is defined if so adds -f for .py command option
ifdef FILE
 LOADFILE = -f$(FILE) 
else
 LOADFILE := 
endif


#options

#Checks serial communication
checkPort:
	@python TELITLOADER/testSerial.py	 #@ makes it silent
	#@echo $(SOURCEFILES) 			 #For debug
	
#Lists all loaded files
list:
	@python TELITLOADER/listAll.py
	
#Checks to see if a file is loaded on telit
find:
	@python TELITLOADER/findFile.py $(LOADFILE)

#Read specific file
read:
	@python TELITLOADER/readFile.py $(LOADFILE)

#READ specific file
delete:
	@python TELITLOADER/deleteFile.py $(LOADFILE)

#Delete all files
deleteAll:
	@python TELITLOADER/deleteAll.py

#Upload specific file
upload:
	@python TELITLOADER/writeFile.py $(LOADFILE)

#Upload and reads back file for error checking
uploadCheck:
	@python TELITLOADER/writeCheck.py $(LOADFILE)

#Enables main file
uploadAll: 
	@echo $(SOURCEFILES)
	for s in $(SOURCEFILES); do \
		echo $ $$s; \
		python TELITLOADER/writeFile.py -f$$s; \
	done
#Enables main script	
enable:
	@python TELITLOADER/enableScript.py $(LOADFILE)
	
#Checks which is main file
checkEnable:
	@python TELITLOADER/enableCheck.py

help:
	@echo -e "HELP:\n" \
	"To use loader just type \"make\" and the command you want \n"\
	"EG: make upload FILE=myfile.py\n"\
	"COMMANDS: \n"\
	"checkPort 			: checks the serial connection and sees if the telits responding. \n"\
	"list 				: lists all files loaded on the telit. \n"\
	"find FILE=myfile.py 		: finds file on Telit, you must type \"FILE=somthing\" to pass file name.\n"\
	"read FILE=myfile.py 		: reads the spicifed file. \n"\
	"delete FILE=myfile.py 		: deletes file from telit. \n"\
	"deleteAll 			: deletes all files on telit \n"\
	"upload FILE=myfile.py		: loads specified file onto telit \n"\
	"uploadAll			: loads all files from the Upload directory onto telit.\n"\
	"uploadCheck FILE=myfile.py	: loads file then reads it back off Telit to make sure it is there \n"\
	"enable FILE=myfile.py		: enables the specified file as the main file to exicute on Telit  \n"\
	"checkEnable			: checks which file is enabled on Telit  \n"\
	
	
	
	
#phony's have no file!
.PHONY:checkPort, list, find, read, delete, deleteAll, upload, uploadAll, uploadCheck, enable, checkEnable



