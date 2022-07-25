# Pharmacophore_modeling_RdRp
This repository is provided to assist development of pharmacophore models reported in the article 'In silico characterization of aryl benzoyl hydrazide derivatives as potential inhibitors of RdRp enzyme of H5N1 influenza virus' authored by Abhishek Ghosh et al.
# Structure based pharmacophore
Two Jupyter notebook files may be used for the developement of strcuture based pharmacophore and screening of ligands with the modified structure based pharmacophore. The strbased_pharmacophore_development.ipynb requires open-access tool Openpharmacophore (available at https://github.com/uibcdf/OpenPharmacophore).
# Ligand based pharmacophore
Two python files (alignment.py and align_ligands.py) may be used for rigid-body alignment performed in the above-mentioned work. The alignment.py may be run with the following command:
python alignment.py --inp input_structures
