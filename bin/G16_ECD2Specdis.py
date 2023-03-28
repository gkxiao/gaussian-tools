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
# This script will extract SpecDis ECD from Gaussian 09/16 TD-DFT calculation output file at APFD/6-311+g(2d,p) level
#
if len(sys.argv) < 3:
    print("")
    print("")
    print("usage:  ")
    print(sys.argv[0]," <TD-DFT output file> <Output file>")
    print("For example:")
    print(sys.argv[0],"CONF_1_ecd.log CONF_1.cd.bil")
    print("CONF_1.cd.bil can be visualized with SpecDis.")
    print("Any question, Please feel free to contact me. info@molcalx.com")
    sys.exit()

#
#
ofile = sys.argv[2]
tddft = sys.argv[1]
if not os.path.exists(tddft):
   #message = "Sorry, I cannot find the "%s" file."
   print("Sorry, cannot find the %s file" % tddft)
   sys.exit()
ecd = open(tddft,'r')
ecdlines = ecd.readlines()
ecd.close()
ecd_n = len(ecdlines)


wavelength = []
rotational = []
for i in range(ecd_n):
    if ('Excited State' in ecdlines[i]):
        wavelength.append(float(ecdlines[i].split()[6].strip()))
    if ('R(length)' in ecdlines[i]):
        vstarter = i + 1
    if ('state          X           Y           Z        Dip. S.   Osc.(frdel)' in ecdlines[i]):
        vend = i - 1
v = range(vstarter,vend)
for i in range(vstarter,vend):
    rotational.append(float(ecdlines[i].split()[-1].strip()))
nstate = len(wavelength)

# print wavelength and rotational strength
# for i in range(nstate):
#     print(wavelength[i],"\t",round(rotational[i],6))

# write output file
oecd = open(ofile,'w')
oecd.write('SpecDis bil-file (length formalism) wavelength (nm)       rotational strength (10**-40 esu**2-cm**2)\n')
for i in range(nstate):
    content = str(wavelength[i])+"\t"+str(rotational[i])+"\n"
    oecd.write(content)
oecd.close
