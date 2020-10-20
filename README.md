# gaussian-tools
1. RDKitSdf2Gau.py   convert MDL SDF file (single molecule) to Gaussian input file 
Usage:
python RDKitSdf2Gau.py -h

2. g2slurm.py        Generate SLURM queue script for Gaussian input file
Usage:
python g2slurm.py -h


3. G16Scan2CONF.py  Extract conformer from scan task output file
Usage:
python G16Scan2CONF.py -h

For each conformer, a torsion-fixed optimization Gaussian input file will be generated.
