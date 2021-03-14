#!/bin/python
# -*- coding: utf-8 -*-
import sys,string,argparse
from optparse import OptionParser
parser = argparse.ArgumentParser(description="Extract Dihedral degree and energy from optimization")
parser.add_argument('goutfile',metavar='<opt output file>',help="Gaussian output file")
args = parser.parse_args()
ifile = args.goutfile


g16log = open(ifile,"r")
gout=g16log.readlines()
g16log.close

# Read ID
id = ifile.split(".")[0]

#Read Frozen Dihedral
for i in range(len(gout)):
    if 'Frozen' in gout[i]:
        D = float(gout[i].split()[3])
        if D < 0 :
            D = float(D) + 360.0
        if D > 180 :
            D = float(D) - 360.0

#Read Energy
E = []
for i in range(len(gout)):
    if 'SCF Done' in gout[i]:
        energy = gout[i].split()[4]
        E.append(energy)

print(id,D,E[-1])