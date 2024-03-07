#!/usr/bin/env python
def xyz2gau(xyzfile,charge,solvent,gauinp):
    """
    create Gaussian 16 constrained OPT input file from xyz.
    """
    prefix_xyzfile,format=xyzfile.split('.')
    solvent=str(solvent)
    check = '%chk='+prefix_xyzfile+'_VCD.chk'

    route = '# FREQ=VCD B3LYP/DEF2TZVP  EmpiricalDispersion=(gd3bj) SCRF=(IEFPCM,Solvent='+solvent+')'
    fout = open(gauinp,'w') 
    fout.write(check+'\n')
    fout.write(route+'\n')
    fout.write('\n')
    fout.write('Structure: '+prefix_xyzfile+' | Job: FREQ=VCD at B3LYP-D3BJ/DEF2-TZVP level\n')
    fout.write('\n')
    fout.write(charge+' 1\n')
    f=open(xyzfile,'r')
    lines = f.readlines()
    f.close()
    for i in range(2,len(lines)):
        fout.write(lines[i])
    fout.write('\n')
    fout.close()
if __name__ == "__main__":
    import sys,string,argparse
    from optparse import OptionParser
    parser = argparse.ArgumentParser(description="Create Gaussian input file (VCD spectra) from XYZ file.\n")
    parser.add_argument('xyzfile',metavar='<Input>',help="input XYZ file")
    parser.add_argument('charge',metavar='<charge>',help="formal charge")
    parser.add_argument('solvent',metavar='<solvent>',help="Solvent:Methanol,cholorform,Acetonitrile")
    parser.add_argument('output',metavar='<Output>',help="Gaussian 16 input file")
    args = parser.parse_args()
    xyzfile = args.xyzfile
    charge = args.charge
    output = args.output
    solvent = args.solvent
    xyz2gau(xyzfile,charge,solvent,output)
