#!/bin/python
import sys,string,argparse
from optparse import OptionParser
parser = argparse.ArgumentParser(description="Generate SLURM SBATCH script for Gaussian 16 job")
parser.add_argument('g16in',metavar='<input>',help="Gaussian 16 input file.")
parser.add_argument('slurmout',metavar='<output>', help="SLURM SBATCH file")
parser.add_argument('nproc', type=int, metavar='<nproc>', help="Number of processor")
parser.add_argument('mem', type=str, metavar='<memory>', help="Memory to be used by G16. For example: 6GB")
parser.add_argument('logprefix',metavar="<prefix>", help="Prefix for SLURM output and error log files")
args = parser.parse_args()
ifile = args.g16in
ofile = args.slurmout
nproc = args.nproc
mem = args.mem
prefix = args.logprefix
slurmout = open(ofile,"w")
slurmout.write('#!/bin/sh\n')
slurmout.write('#SBATCH -N 1\n')
slurmout.write('#SBATCH -o '+prefix+'_out.%j\n')
slurmout.write('#SBATCH -e '+prefix+'_err.%j\n')
slurmout.write('cd  $SLURM_SUBMIT_DIR\n')
slurmout.write('source ~/bin/g16_env.sh\n')
slurmout.write('$g16root/g16/g16 -p='+str(nproc)+' -m='+mem+' '+ifile+' \n')
slurmout.close
