import sout
import MOD
import GPS
#import string

def currentPosition():
	pos = {}
	res = GPS.getActualPosition()
	tmp = res.split(',')
	#tmp = string.split(res,',') #for testing on mac
	pos['time'] = tmp[0]
	pos['lat'] = parseDMS(tmp[1])
	pos['lon'] = parseDMS(tmp[2])
	pos['hdop'] = tmp[3]
	pos['alt'] = tmp[4]
	pos['fix'] = tmp[5]
	pos['cog'] = tmp[6]
	pos['spkm'] = tmp[7]
	pos['spkn'] = tmp[8]
	pos['date'] = tmp[9]
	pos['nr_sat'] = tmp[10]
	return pos

#converts string to tuple
def parseDMS(dms):
	if len(dms) < 10: #don't have a good fix
		return (0,0,0,'X')
	#dms formatted like: (D)DDMM.SSSSC
	c = dms[-1] #cardinal direction
	s = int(int(dms[-5:-1])/100) #seconds
	m = int(dms[-8:-6]) #minutes
	d = int(dms[:-8]) #degrees, either two or three long	
	return d,m,s,c
