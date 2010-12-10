import Debug

gpsIndex = 0

# Concepts that we aim to test with our GPS filtering.  we want to test how we deal with locks
# we also want to deal with different decimal mixtures

#<UTC>,<latitude>,<longitude>,<hdop>,<altitude>,<fix>,<cog>,<spkm>,<spkn>,<date>,<nsat>

#gpsDilutionLock = [['5.0','2'], ['1.0','0'], ['5.1','3'], ['2.9','3'], ['2.09','2'], ['9','0'], ['9','2'], ['5.0','2'], ['5.5','2'], ['2.3','2'], ['1.6','2'], ['1','2'], ['2.0','3'], ['3.4','2']]
#gpsDilutionLock = [['5.4','2'], ['4.3','0'], ['1.5','3'], ['2.9','3'], ['2.09','2'], ['1.45','0'], ['3','2'], ['1.0','2'], ['5.5','2'], ['2.3','2'], ['2.30','2'], ['1.9','2'], ['2.0','0'], ['5','2']]
# below tests the old stale lock concept
gpsDilutionLock = [['5.4','2'], ['4.3','0'], ['1.5','0'], ['1.3','2'], ['2.09','0'], ['1.45','0'], ['3','0'], ['1.0','0'], ['5.5','0'], ['2.3','0'], ['2.30','0'], ['1.9','0'], ['2.0','0'], ['5','0'], ['2.09','0'], ['1.45','0'], ['3','0'], ['1.0','0'], ['5.5','0'], ['2.3','0'], ['2.30','0'], ['1.9','0'], ['2.0','0'], ['5','0']]


def getActualPosition():
	if(Debug.GPSDebugOutput() == 1):
		print 'dummy getActualPosition()'
	
	global gpsIndex
	
	#result = '151956.999,4542.8100N,01344.2665E,1.4,207.5,3,11.78,0.46,0.25,141206,05'
	#return '053053.000,4223.5412N,07106.9411W,1.2,49.4,3,184.24,3.60,1.94,141108,06'
	
	if(gpsIndex >= len(gpsDilutionLock)):
		gpsIndex = 0
	
	t = gpsDilutionLock[gpsIndex]
	
	lock = '053053.000,4223.5412N,07106.9411W,'+t[0]+',49.4,'+t[1]+',184.24,3.60,1.94,141108,06'
	
	if(Debug.GPSDebugOutput() == 1):
		print 'DummyGPS= \'' + lock +'\''
	
	gpsIndex = gpsIndex + 1
	
	return lock	
		

def getPosition():
	if(Debug.GPSDebugOutput() == 1):
		print 'dummy getPosition()'
	return 0, 'N', 0, 'E'

def powerOnOff(onOff):
	print 'GPS powerOnOff ' + str(onOff)
