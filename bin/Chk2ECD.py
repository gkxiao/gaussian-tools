#!/usr/bin/env python
import sys,string,argparse

def chk2gau(oldchk, newchk, chemmodel='APFD/6-311+G(2d,p)', gauinp='ecd.com'):
    """
    Perform ECD simulation with TD-DFT
    """
    title = 'ECD simulation at '+chemmodel+' level'
    oldchkfile = oldchk
    newchkfile = newchk
    route = '#P td=(nstates=100) '+chemmodel+' guess=read geom=allcheck scrf=check'
    fout = open(gauinp,'w')
    fout.write('%oldchk='+oldchkfile+'\n')
    fout.write('%chk='+newchkfile+'\n')
    fout.write(route+'\n')
    fout.write(" \n")
    fout.write(title+"\n")
    fout.write(" \n")
    fout.close()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate Gaussian input file which perform TD-DFT calculation to simulate ECD spectra with IEFPCM solvent model.\n")
    parser.add_argument('oldchkfile',metavar='<old check file>',help="Check file from Opt & Freq calculation.")
    parser.add_argument('newchkfile',metavar='<output check file>',help="Check file for current calculation.")
    parser.add_argument('output',metavar='<Output>',help="G16 input file")
    parser.add_argument('chemmodel',metavar='<chemistry model>',help="Chemistry model used in current calculation. The default model is APFD/6-311+g(2d,p)")
    args = parser.parse_args()
    oldchkfile = args.oldchkfile
    newchkfile = args.newchkfile
    output = args.output
    chemmodel = args.chemmodel
    chk2gau(oldchkfile,newchkfile,chemmodel,output)
