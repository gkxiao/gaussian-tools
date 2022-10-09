#!/usr/bin/env python
from rdkit import Chem
import sys,string,argparse

def mol2gau(mol, gauinp, chemmodel, solvent):
	"""
	Generate Gaussian Opt & Fred input file from MDL SDF file.
	"""
	title = 'Opt Freq at '+chemmodel+' level'
	name = mol.GetProp('_Name')
	route = '#P OPT FREQ '+chemmodel+' scrf=(iefpcm,solvent='+solvent+')' 
	fout = open(gauinp,'w')
	fout.write('%chk='+name+'.chk'+'\n')
	fout.write(route+'\n')
	fout.write(" \n")
	fout.write('Structure: '+name+'\n')
	fout.write('Calculation: '+title+'\n')
	fout.write(" \n")
	n = mol.GetNumAtoms()
	formalcharge = str(Chem.rdmolops.GetFormalCharge(mol))
	fout.write(formalcharge+" 1\n")
	for i in range(n):
		pos = mol.GetConformer().GetAtomPosition(i)
		element = mol.GetAtoms()[i].GetSymbol()
		x = str(round(pos.x,4))
		y = str(round(pos.y,4))
		z = str(round(pos.z,4))
		fout.write(element+" "+x+" "+y+" "+z+'\n')
	fout.write(" \n")
	fout.close()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="""
    Generate Gaussian input file which perform Opt & Freq calculation
    at DFT level with IEFPCM solvent model. 
    For examole:
    ./RDKitSDF2GaussOptInSolvent.py CONF_01.sdf CONF_01_opt_freq.com 'APFD/6-311+g(2d,p)' methanol
    """)
    parser.add_argument('sdffile',metavar='<Input>',help="SDF file with full hydrogen. For example, CONF_01.sdf")
    parser.add_argument('output',metavar='<Output>',help="G16 input file, e.g. CONF_01_min.com")
    parser.add_argument('chemmodel',metavar='<Chemistry model>',help="Chemistry model, e.g. APFD/6-311+G(2d,p). The available DFT method can be found from: https://gaussian.com/dft. And the available basis set can be found from: https://gaussian.com/basissets")
    parser.add_argument('solvent',metavar='<solvent>',help="solvent, the available solvent can be found from: http://gaussian.com/scrf")
    args = parser.parse_args()
    sdffile = args.sdffile
    output = args.output
    chemmodel = args.chemmodel
    solvent = args.solvent
    suppl = Chem.SDMolSupplier(sdffile, removeHs=False)
    mol = suppl[0]
    mol2gau(mol,output,chemmodel,solvent)

