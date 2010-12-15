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




