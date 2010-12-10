PORT=None
BAUD=None
with open("settings.txt") as f: #using with you don't have to call close()
    for line in f:
	line=line.lower()
        args=line.split(" ")
	if args[0] == "port":
		PORT = args[1]
	elif args[0] == "baud":
		BAUD = args[1]
	else:
		 pass

if PORT==None or BAUD==None:
	print "****ERROR BAD SYNTAX -> Check \"settings.txt\" file \n\
Syntax is:\n PORT(space)/dev/myportblah.tty(RETURN)\
\n BAUD(space)9600(RETURN)"

else:
	print "USING##############\nPort: " + PORT + "\n" "Baud: " + BAUD 


