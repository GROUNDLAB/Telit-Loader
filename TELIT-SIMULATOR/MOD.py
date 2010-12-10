import time

def reactivatePython():
  # simulation impossible
  return

def secCounter():
  sec = time.time()
  return int(sec)

def sleep(tenthOfSec):
  sec = float(tenthOfSec)/10
  print "sleeping ",sec,"sec"
  time.sleep(sec)
  return

def powerSaving(seconds):
  print 'dummy powerSaving(', seconds, ')'
  time.sleep(seconds)
  return

def powerSavingExitCause():
  print 'dummy powerSavingExitCause()'
  return 1

def watchdogEnable(seconds):
  print 'dummy watchdogEnable(', seconds, ')'
  return

def watchdogReset():
  print 'dummy watchdogReset()'
  return

def watchdogDisable():
  print 'dummy watchdogDisable()'
  return

