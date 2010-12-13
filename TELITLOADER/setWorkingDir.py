import os
#set your working directory here, since make is called from ../
global workingDir
global codeDir
workingDir = os.getcwd()+"/TELITLOADER/"
codeDir = os.getcwd()+"/UploadCode/"
print
print "#######################################################################################"
print "##YOUR CURRENT WORKING DIR IS: " 
print workingDir
print "##YOUR CURRENT UPLOAD DIRECTORY IS:"
print codeDir
print "####################################################################################### "
print
os.chdir(workingDir)
