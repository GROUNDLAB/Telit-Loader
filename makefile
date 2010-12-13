#MAKEFILE to load to telit


SOURCEFILESDIR=  $(wildcard UploadCode/*.py)
SOURCEFILES= $(notdir $(SOURCEFILESDIR))
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
	#Delete specific file
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
	
.py:	
	@python TELITLOADER/writeFile.py $(notdir $@)

enable:
	@python TELITLOADER/enableScript.py $(LOADFILE)
	#Checks which is main file
checkEnable:
	@python TELITLOADER/enableCheck.py

#phony's have no file!
.PHONY:checkPort, list, find, read, delete, deleteAll, upload, uploadAll, uploadCheck, enable, checkEnable
