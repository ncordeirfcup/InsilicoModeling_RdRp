from rdkit import Chem
from rdkit.Chem import rdMolDescriptors
from rdkit.Chem import rdMolAlign
from conformers import generate_conformers
import numpy as np
import copy

def align_set_of_ligands(ligands):
    """ Align a set of ligands to each other

        Parameters
        ----------
        ligands : list of rdkit.Chem.rdchem.Mol or rdkit.Chem.SmilesMolSupplier or rdkit.Chem.SDMolSupplier
            List of ligands.
        
        Returns
        ----------
        aligned_molecules : list of rdkit.Chem.rdchem.Mol
            List of aligned ligands.
        
        crippen_score : list of float
            List with crippen scores calculated during the alignment.

    """
    
    if not isinstance(ligands, list):
        ligands = list(ligands)

    molecules2 = copy.deepcopy(ligands)
    molecules = [generate_conformers(mol, 100) for mol in molecules2]
    #molecules = [generate_conformers(mol, 500) for mol in molecules2]
    #print('The length of ligands'+str(len(molecules2)))
    print('the length of conformation file'+str(len(molecules)))

    crippen_contribs = [rdMolDescriptors._CalcCrippenContribs(mol) for mol in molecules]
    crippen_ref_contrib = crippen_contribs[0]
    crippen_prob_contribs = crippen_contribs

    ref_mol = molecules[0]
    probe_mols = molecules

    crippen_score = []
    aligned_molecules = []
    for idx, mol in enumerate(probe_mols):
        tempscore = []
        
        for cid in range(100):
            try: 
               crippenO3A = rdMolAlign.GetCrippenO3A(mol, ref_mol, crippen_prob_contribs[idx], crippen_ref_contrib, cid, 0)
            except ValueError:
               print(mol,cid)
               continue
            crippenO3A.Align()
            tempscore.append(crippenO3A.Score())
            
        best = np.argmax(tempscore)
        mol_string = Chem.MolToMolBlock(mol, confId=int(best))
        temp_mol = Chem.MolFromMolBlock(mol_string, removeHs=False)
        
        crippen_score.append(tempscore[best])
        aligned_molecules.append(temp_mol)
    print(len(aligned_molecules))
    print(crippen_score)
    
    return aligned_molecules, crippen_score
        
    