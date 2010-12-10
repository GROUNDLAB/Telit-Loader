import MDM

def sendAT(cmd):
	MDM.send(cmd + '\r', 0)
	res = MDM.receive(30)
	if (res.find('OK') == -1):
		print 'cmd: %s failed: %s' % (cmd, res)
		return 0
	return 1

def initModem():
	if (not sendAT('AT')):
		return 0
	if (not sendAT('AT+IPR=9600')):
		return 0
	if (not sendAT('AT+CMEE=2')):
		return 0
	res = MDM.send('AT+CPIN=1234\r', 0)	# insert your pin
	res = MDM.receive(3)
	# ignore error, maybe pin is already set
	return 1

def initGprs():
	if (not sendAT('AT+CGDCONT=1,"IP","internet.eplus.de","0.0.0.0",0,0')):
		return 0
	if (not sendAT('AT#USERID="eplus"')):
		return 0
	if (not sendAT('AT#PASSW="eplus"')):
		return 0
	return 1

def switchGprsOn():
	if (not sendAT('AT#GPRS=1')):
		return 0
	return 1

def switchGprsOff():
	if (not sendAT('AT#GPRS=0')):
		return 0
	return 1

def gprsIsOn():
	MDM.send('AT#GPRS?\r', 0)
	res = MDM.receive(10)
	print 'GPRS on: ' + res
	if (res.find('1') == -1):
		return 0
	else:
		return 1