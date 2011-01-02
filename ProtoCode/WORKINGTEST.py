
#####TAKE ME OUT BEFORE UPLOADING!!!!!!!##########
import sys
import fileinput
sys.path.append('../TELIT-SIMULATOR')
#####END TAKE OUT#################################

import GPS
import SER
import MDM
import MOD

SER.set_speed('9600')
while 1:
	SER.send('hello world!')
	MOD.sleep(30)

