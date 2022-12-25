# Pharmacophore_modeling_RdRp
This repository is provided to assist development of pharmacophore models reported in the article 'In silico characterization of aryl benzoyl hydrazide derivatives as potential inhibitors of RdRp enzyme of H5N1 influenza virus' authored by Abhishek Ghosh et al.

The following dependencies are required to be installed: Numpy, Pandas, RDKit

# Structure based pharmacophore
Two Jupyter notebook files may be used for the developement of strcuture based pharmacophore and screening of ligands with the modified structure based pharmacophore. The strbased_pharmacophore_development.ipynb requires open-access tool Openpharmacophore (available at https://github.com/uibcdf/OpenPharmacophore).
# Ligand based pharmacophore
Two python files (alignment.py and align_ligands.py) may be used for rigid-body alignment performed in the above-mentioned work. The alignment.py may be run with the following command:

python alignment.py --inp input_structures

The aligned structures will be saved as input_structures_aligned.sdf

#2D-QSAR modeling
The users may generate the 2D-QSAR models reported in the current work by using the training and test set files provided in the current repository (as .csv files) and by using the web-based app https://amit-mlr.herokuapp.com/. In this app, the user needs to upload the training and test set files (without changing their names) and put 'Dependent variable column' as 'last' to check the details of the 2D-QSAR models (such as corrlation matrix, predicted activity, plots, etc).

#Citation
GHOSH, A., PANDA, P., HALDER, A. K. & CORDEIRO, M. N. D. S. 2022. In silico characterization of aryl benzoyl hydrazide derivatives as potential inhibitors of RdRp enzyme of H5N1 influenza virus. Frontiers in Pharmacology, 13.
