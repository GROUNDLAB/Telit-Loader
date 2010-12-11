#MAKEFILE to load to telit
ifdef FILE
 LOADFILE = -f$(FILE) 
else
 LOADFILE := 
endif

port:
	@python setport.py #@ makes it silent

upload:
	@python upload.py $(LOADFILE)

list:
	python list.py
#phony's have no file!
.PHONY:port, list, read, delete, upload, uploadAll
