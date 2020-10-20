def mol2gau(mol, gauinp):
	from rdkit import Chem
	"""
	Convert RDKIT mol into Gaussian input file.
	"""
	title = 'Opt Freq at APFD/6-311+g(2d,p) level'
	name = mol.GetProp('_Name')
	route = '#P OPT FREQ APFD/6-311+g(2d,p)'
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
	fout.write(" \n")
	fout.close()

if __name__ == "__main__":
	from rdkit import Chem
	import sys,string,argparse
	from optparse import OptionParser
	
	parser = argparse.ArgumentParser(description="Convert SDF to Gaussian input file.\n")
	parser.add_argument('sdffile',metavar='<Input>',help="SDF file with full hydrogen")
	parser.add_argument('output',metavar='<Output>',help="G16 input file")
	args = parser.parse_args()
	sdffile = args.sdffile
	output = args.output
	suppl = Chem.SDMolSupplier(sdffile, removeHs=False)
	mol = suppl[0]
	mol2gau(mol,output)
