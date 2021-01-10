#!/bin/python
# -*- coding: utf-8 -*-
import sys,string,argparse
from optparse import OptionParser
parser = argparse.ArgumentParser(description="Extract conformer from Gaussian torsion scan")
parser.add_argument('goutfile',metavar='<scan output file>')
args = parser.parse_args()
ifile = args.goutfile

#no_atom = args.no_atom
charge = 0
Multiplicity = 1
AddInp = "\n"
#Read the result of torsion scan at PM7 level
g16log = open(ifile,"r")
gout=g16log.readlines()
g16log.close

#提取电荷与自旋多态性
line_atom_start = 0
for i in range(len(gout)):
    if 'Symbolic Z-matrix' in gout[i]:
        line_atom_start = i + 2
        charge_Multip = gout[i+1].split()
        charge = gout[i+1].split()[2]
        Multiplicity = gout[i+1].split()[5]

# atom number 2 element
def GetAtomSymbol(AtomNum):
    Lookup = ['H', 'He', 'Li', 'Be', 'B', 'C', 'N', 'O', 'F', 'Ne', 'Na', 'Mg', 'Al', \
              'Si', 'P', 'S', 'Cl', 'Ar', 'K', 'Ca', 'Sc', 'Ti', 'V', 'Cr', 'Mn', 'Fe', 'Co', \
              'Ni', 'Cu', 'Zn', 'Ga', 'Ge', 'As', 'Se', 'Br', 'Kr', 'Rb', 'Sr', 'Y', 'Zr', \
              'Nb', 'Mo', 'Tc', 'Ru', 'Rh', 'Pd', 'Ag', 'Cd', 'In', 'Sn', 'Sb', 'Te', 'I', \
              'Xe', 'Cs', 'Ba', 'La', 'Ce', 'Pr', 'Nd', 'Pm', 'Sm', 'Eu', 'Gd', 'Tb', 'Dy', \
              'Ho', 'Er', 'Tm', 'Yb', 'Lu', 'Hf', 'Ta', 'W', 'Re', 'Os', 'Ir', 'Pt', 'Au', \
              'Hg', 'Tl', 'Pb', 'Bi', 'Po', 'At', 'Rn']

    if AtomNum > 0 and AtomNum < len(Lookup):
        return Lookup[AtomNum-1]
    else:
        print("No such element with atomic number " + str(AtomNum))
        return 0
        
#提取Dihedral
line_atom_end = 0
for i in range(len(gout)):
    if 'The following ModRedundant input section has been read' in gout[i]:
        line_atom_end = i - 2
        dihedral=gout[i+1].split()
AddInp = str(dihedral[1])+' '+str(dihedral[2])+' '+str(dihedral[3])+' '+str(dihedral[4])+' F'        

no_atom = line_atom_end - line_atom_start + 1
#提取全部的构象
CONF = []
for i in range(len(gout)):
    if 'Input orientation' in gout[i]:
        start = i + 5
        end = i + 5 + int(no_atom)
        CONF.append(gout[start:end])

#建立收敛的索引
ConfIndex = []
n = 0
for i in range(len(gout)):
    if 'Maximum Force' in gout[i]:
        n = n + 1
        if 'Optimization completed' in gout[i+5]:
            ConfIndex.append(n)
print("Total Conformer number:",len(ConfIndex))

#遍历构象，获取索引号
for n in range(len(ConfIndex)):
    index = ConfIndex[n]-1
    #获得构象
    #CONF[index]
    #保存构象
    id = n+1
    ofile = open("CONF_"+str(id)+".gjf","w")
    slurmout = open("CONF_"+str(id)+".sbatch","w")
    ofile.write('%chk=CONF_'+str(id)+'.chk\n')
    ofile.write('# opt=modredundant apfd/6-311+g(2d,p) nosymm\n')
    ofile.write('\n')
    ofile.write('QM-Torsion Profling at apfd/6-311+g(2d,p) level\n')
    ofile.write('\n')
    ofile.write(str(charge)+' '+str(Multiplicity)+'\n')
    for i in range(int(no_atom)):
        gid,atom,no,x,y,z=CONF[index][i].split()
        atom = GetAtomSymbol(int(atom))
        ofile.write(atom+' '+x+' '+y+' '+z+'\n')
    ofile.write('\n')
    ofile.write(AddInp+'\n')
    ofile.write('\n')
    slurmout.write('#!/bin/bash\n')
    slurmout.write('#SBATCH -N 1\n')
    slurmout.write('#SBATCH -o CONF_'+str(id)+'_out.%j\n')
    slurmout.write('#SBATCH -e CONF_'+str(id)+'_err.%j\n')
    slurmout.write('cd  $SLURM_SUBMIT_DIR\n')
    slurmout.write('source ~/bin/g16_env.sh\n')
    slurmout.write('GAUSS_SCRDIR=`mktemp -d ./gauss.XXXXX`\n')
    slurmout.write('export GAUSS_SCRDIR\n')
    slurmout.write('$g16root/g16/g16 -p=16 -m=12GB CONF_'+str(id)+'.gjf\n')
ofile.close
slurmout.close
