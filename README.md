# Random Forest for the identification of relationships between epigenetic marks and its application to robust assignment of chromatin states
This approach is implemented in Python 3.7. Please follow specific instructions for your platform to install the Python 3 interpreter [here](https://www.python.org/downloads/).
## Requirements
- scikit-learn == 0.24.2
- numpy ==  1.19.5
- pandas == 1.1.2
- scipy == 1.5.4
- joblib == 1.0.0
# Dataset creation
For the dataset creation, is necesary have all ChIP-seq data in Bedgraph format. The dataset will be created by chromosome, for this we use the script extract_chr.py to divide our data.
```
python3 extract_chr.py -I input_file.bedgraph -C chromosome
```

The second step is use the script dataset_bedgraph.py to convert own data to a table that divided in fragments of *n* bases of size. In this study we use a *n* value of 2000.
```
python3 dataset_bedgraph.py -I input_file_1.bedgraph input_file_2.bedgraph ... input_file_n.bedgraph -W n_size(int)
```

Then, our approach considers fragments upstream and downstream to the site in which we want to predict. For this, the script datasets_distance_parallel.py was used. This script needs as input arguments the output file of dataset_bedgraph.py, the number of bases to condider upstream and downstream, the size of fragments (same number use of the previous script) and the number of cores to use (this script allows to parallelize the task).
```
python3 datasets_distance_parallel.py output_dataset_bedgraph_file.tsv distance(int) fragment_size(int) n_cores(int)
```

