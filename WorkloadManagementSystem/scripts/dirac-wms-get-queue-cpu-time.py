#!/usr/bin/env python
########################################################################
# File :    dirac-wms-get-queue-cpu-time.py
# Author :  Federico Stagni
########################################################################
""" Report CPU length of queue, in seconds
    This script is used by the dirac-pilot script to set the CPUTime left, which is a limit for the matching
"""
__RCSID__ = "$Id$"

import DIRAC
from DIRAC.Core.Base import Script

Script.registerSwitch( "C:", "CPUNormalizationFactor=", "CPUNormalizationFactor, in case it is known" )

Script.setUsageMessage( '\n'.join( [ __doc__.split( '\n' )[1],
                                     'Usage:',
                                     '  %s [option|cfgfile]' % Script.scriptName ] ) )
Script.parseCommandLine( ignoreErrors = True )
args = Script.getPositionalArgs()

CPUNormalizationFactor = 0.0
for unprocSw in Script.getUnprocessedSwitches():
  if unprocSw[0] in ( "C", "CPUNormalizationFactor" ):
    CPUNormalizationFactor = float( unprocSw[1] )

if __name__ == "__main__":
  from DIRAC.WorkloadManagementSystem.Client.CPUNormalization import getCPUTime
  cpuTime = getCPUTime( CPUNormalizationFactor )
  DIRAC.gLogger.info( 'Queue CPU time:', str( cpuTime ) )
  DIRAC.exit( 0 )
