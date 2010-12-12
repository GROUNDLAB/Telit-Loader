#MAKEFILE to load to telit



#checks if FILE is defined if so adds -f for .py command option
ifdef FILE
 LOADFILE = -f$(FILE) 
else
 LOADFILE := 
endif

checkPort:
	@python setport.py #@ makes it silent

listFile:
	@python list.py

readFile:
	@python

deleteFile:
	@python

deleteAll:
	@python

uploadFile:
	@python commands.py $(LOADFILE)

uploadCheck:
	@python


#phony's have no file!
.PHONY:checkPort, listFile, readFile, deleteFile, uploadFile, uploadCheck, uploadAll
