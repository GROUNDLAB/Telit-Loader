#dummy class to test compilation
import time
def send(string):
	print string
def sendbyte(byte):
	print hex(byte)
def set_speed(bitrate):
	print "[SER] setting bitrate:" + bitrate
def receive(timeout):
	input="no input"
	print "[SER] wating:"+timeout+" seconds from keyboard input, type something"
	timer = time.time()+timeout
	while time.time()<timer:
		#read input
		time.sleep(1)	#can't hammer CPU
		input = sys.stdin.readlines()
	return input
