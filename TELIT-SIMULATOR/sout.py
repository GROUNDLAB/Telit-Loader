import SER
import sys

class serialStdOut:
	def __init__(self, desc):
		self.desc = desc
		self.term = '\r'

	def write (self, s):
		SER.send(self.desc + s.rstrip() + self.term)
		
SER.set_speed('115200', '8N1')
#enable these lines on the telit, but not on the mac
#sys.stdout = serialStdOut("")
#sys.stderr = serialStdOut("stderr: ")
print "stdout initialized"