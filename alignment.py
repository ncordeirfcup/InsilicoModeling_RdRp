import copy
from rdkit import Chem
from rdkit.Chem import Draw
from rdkit.Chem.Draw import IPythonConsole
from rdkit.Chem import AllChem
from rdkit.Chem import rdBase
from rdkit.Chem import rdMolAlign
from rdkit.Chem import rdMolDescriptors
import numpy as np

from align_ligands import align_set_of_ligands
import argparse
def main():
    parser=argparse.ArgumentParser(description='import sdf')
    parser.add_argument('--inp', help='sdf input file name')
    #parser.add_argument('--out',type=argparse.FileType('r'), help='sdf output file name to be saved')
    args=parser.parse_args()
    name=str(args.inp)+'.sdf'
    mols = [m for m in Chem.SDMolSupplier('./'+name) if m != None]
    aligned_molecules, crippen_score=align_set_of_ligands(mols)
    outn=str(args.inp)+'_out.sdf'
    writer = Chem.SDWriter(outn)
    for n in range(len(aligned_molecules)):
        writer.write(aligned_molecules[n])
    writer.close()

if __name__=='__main__':
   main()
