#!/usr/bin/env python
import sys,string,argparse

def chk2gau(oldchk, newchk, gauinp):
    """
    Perform NMR simulation at mPW1PW91/6-311g+(2d,p) level with GIAO method.
    """
    title = 'Simulate NMR spectra at mPW1PW91/6-311+G(2d,p) level'
    oldchkfile = oldchk
    newchkfile = newchk
    route = '#P mPW1PW91/6-311+G(2d,p) guess=read geom=allcheck scrf=check'
    fout = open(gauinp,'w')
    fout.write('%oldchk='+oldchkfile+'\n')
    fout.write('%chk='+newchkfile+'\n')
    fout.write(route+'\n')
    fout.write(" \n")
    fout.write(title+"\n")
    fout.write(" \n")
    fout.close()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate Gaussian input file which perform NMR calculation at mPW1PW91/6-311+g(2d,p) level with IEFPCM solvent model.\n")
    parser.add_argument('oldchkfile',metavar='<old check file>',help="Check file from Opt & Freq calculation.")
    parser.add_argument('newchkfile',metavar='<output check file>',help="Check file for current calculation.")
    parser.add_argument('output',metavar='<Output>',help="G16 input file")
    args = parser.parse_args()
    oldchkfile = args.oldchkfile
    newchkfile = args.newchkfile
    output = args.output
    chk2gau(oldchkfile,newchkfile,output)
