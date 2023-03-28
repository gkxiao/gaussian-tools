#!/usr/bin/env python
import sys,re,os

#
# Author: Gaokeng Xiao
# Email: info@molcalx.com
# @ Phone: 020-38261356
# Organization: Guangzhou Molcalx.Information & Technology Ltd
# Home page: http://www.molcalx.com.cn.
# Date: 2017-09-06
# Version: 0.1
#
# This script will extract VCD spectra from Gaussian 16 output file
#
if len(sys.argv) < 3:
    print("")
    print("")
    print("usage:  ")
    print(sys.argv[0]," <Gaussian  output file> <VCD spectra output file>")
    print("")
    print("For example:")
    print(sys.argv[0],"CONF_01_VCD.log CONF_01.vc.bil")
    print('')
    print('The output file CONF_01.vc.bil can be visualized with Specdis.')
    print('')
    print("Any question, Please feel free to contact me. info@molcalx.com")
    print('')
    sys.exit()

#
# input file
ifile = sys.argv[1]
if not os.path.exists(ifile):
   print("Sorry, I cannot find the %s file" % ifile)
   sys.exit()

# Output file
ofile = sys.argv[2]
if os.path.exists(ofile):
   print("The output file, %s, already exists, please use another one, Existing..." % ofile)
   sys.exit()


# read nwchem output file
file = open(ifile,'r')
lines = file.readlines()
file.close()
n = len(lines)

# extract wavelength/frequency
wavelengths = []
for i in range(n):
    if ('Frequencies' in lines[i]):
        line = re.split(r"[ ]+",lines[i])
        for x in line[3:]:
            wavelength = float(x.strip())
            wavelengths.append(wavelength)

# extract rotational strength
rotational_strengths = []
for i in range(n):
    if ('Rot. str.' in lines[i]):
        line = re.split(r"[ ]+",lines[i])
        for x in line[4:]:
            rotational_strength = float(x.strip())
            rotational_strengths.append(rotational_strength)
# export Spedis VCD spectra
vcd_ofile = open(ofile,'w')
vcd_ofile.write('SpecDis bil-file VCD (wavenumber (cm**-1)   rotational strength (10**-44 esu**2-cm**2))\n')
for i in range(len(wavelengths)):
    content = str(wavelengths[i])+"\t"+str(rotational_strengths[i])+"\n"
    vcd_ofile.write(content)
vcd_ofile.close()

