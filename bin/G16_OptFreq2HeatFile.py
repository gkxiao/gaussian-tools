#!/usr/bin/env python
import sys
import string
import os

#
# Author: Gaokeng Xiao
# Email: info@molcalx.com
# @ Phone: 020-38261356
# Organization: Guangzhou Molcalx.Information & Technology Ltd
# Home page: http://www.molcalx.com.cn.
# Date: 2017-09-06
# Version: 0.1
#
# This script will extract HF  at DFT level
#
if len(sys.argv) < 3:
    print("")
    print("")
    print("usage:  ")
    print(sys.argv[0]," <DFT opt freq output file>  <Output heat file>")
    print("For example:")
    print(sys.argv[0],"CONF_1_min.log CONF_1_min.heat")
    print("CONF_1_min.heat will be use to calculate Boltzmann's weight for Specdis")
    print("Any question, Please feel free to contact me. info@molcalx.com")
    sys.exit()

#
#
ofile = sys.argv[2]
optfreq = sys.argv[1]
if not os.path.exists(optfreq):
   #message = "Sorry, I cannot find the "%s" file."
   print("Sorry, I cannot find the %s file" % gaussoutput)
   sys.exit()
optfreqfile = open(optfreq,'r')
optfreqlines = optfreqfile.readlines()
optfreqfile.close()
of_n = len(optfreqlines)
#
# Gaussian job check
#
if not ('Normal termination' in optfreqlines[-1]):
   print("The Gaussian job is not terminated normally. Please check it!")
   sys.exit()

#

# extract free  Energy
for i in range(of_n):
    if ('Sum of electronic and thermal Free Energies' in optfreqlines[i]):
        G = float(optfreqlines[i].split()[-1].strip("\n"))*627.5049

#
oheat = open(ofile,'w')
oheat.write('HEAT OF FORMATION  =  '+str(G))

