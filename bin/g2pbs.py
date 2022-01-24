#!/bin/python
import sys,string,argparse
from optparse import OptionParser
parser = argparse.ArgumentParser(description="Generate PBS/SGE script for Gaussian 16 job")
parser.add_argument('g16in',metavar='<input>',help="Gaussian 16 input file.")
parser.add_argument('pbsout',metavar='<output>', help="PBS file")
parser.add_argument('nproc', type=int, metavar='<nproc>', help="Number of processor")
parser.add_argument('mem', type=str, metavar='<memory>', help="Memory to be used by G16. For example: 6GB")
parser.add_argument('logprefix',metavar="<prefix>", help="Prefix for SLURM output and error log files")
args = parser.parse_args()
ifile = args.g16in
ofile = args.pbsout
nproc = args.nproc
mem = args.mem
prefix = args.logprefix
output = open(ofile,"w")
output.write('#!/bin/sh\n')
output.write('#PBS -o '+prefix+'_out.%j\n')
output.write('#PBS -e '+prefix+'_err.%j\n')
output.write('#PBS -l nodes=1:ppn='+str(nproc)+'\n')
output.write('cd  $PBS_O_WORKDIR\n')
output.write('source ~/bin/g16_env.sh\n')
output.write('$g16root/g16/g16 -p='+str(nproc)+' -m='+mem+' '+ifile+' \n')
output.close
