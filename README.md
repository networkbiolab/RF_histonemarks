# Random Forest for the identification of relationships between epigenetic marks and its application to robust assignment of chromatin states
This approach is implemented in Python 3.7. Please follow specific instructions for your platform to install the Python 3 interpreter [here](https://www.python.org/downloads/).
## Requirements
- scikit-learn == 0.24.2
- numpy ==  1.19.5
- pandas == 1.1.2
- scipy == 1.5.4
- joblib == 1.0.0
# Dataset creation
For the dataset creation, is necesary have all ChIP-seq data in Bedgraph format. The dataset will be created by chromosome  First we use the script dataset_bedgraph.py to convert own data to a table in the 
