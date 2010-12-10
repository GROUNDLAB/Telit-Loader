import sout 
import GPIO
import MOD

print "gpio test"

for i in range(10):
	GPIO.setIOvalue(12, 1)
	print "on"
	MOD.sleep(10)
	GPIO.setIOvalue(12,0)
	print "off"
	MOD.sleep(10)
