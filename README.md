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

Then, our approach considers fragments upstream and downstream to the site in which we want to predict. For this, the script datasets_distance_parallel.py was used. This script needs as input arguments the output file of dataset_bedgraph.py, the number of bases to condider upstream and downstream, the size of fragments (same number use of the previous script) and the number of cores to use (this script allows to parallelize the task). In this work a distance value of 10000 bases was used.
```
python3 datasets_distance_parallel.py output_dataset_bedgraph_file.tsv distance(int) fragment_size(int) n_cores(int)
```

To extract the attributes or a subset of attributes of our generated dataset, and generate the labels of the histone marks to train the Random Forest. The script mega_subset_bedgraph.py can help us. This script use as input arguments the file of the datasets which we want to extract the data, a file with the name of attributes and the label of the histone mark to predict, the name of the output file, the distance upstream and downstream and fragment size used to create the dataset.
```
python3 mega_subset_bedgraph.py dataset.tsv attributes_to_extract.txt output_file_name distance(int) fragment_size(int)
```

An example of the format of the file attributes_to_extract.txt is as follows:
```
H3K4ME1
H3K4ME2
H3K4ME3
H3K27AC_label
```
# Train and Test Random Forest algorithms
The next step is use the created dataset to train and test the Random Forest algorithms. For this, we use the script RF_regression_load.py. This script has two options of usage, the first (0) use the entire dataset to train the algorithms, and the second (1) loads a model and test it with the given dataset. The output of this script are the trained model in format .pkl and and the importance values of the attributes used. The input arguments of the script using the first option (0) are the dataset file, number of trees, depth (0 to max depth) and number, cores and the name of the histone mark to predict.
```
python3 RF_regression_load.py 0 dataset.tsv n_trees(int) depth(int) n_cores(int) histone_mark_name
```
The input arguments of the second option (1) are the model to test in .pkl format, the dataset to test, and the predicted histone mark.
```
python3 RF_regression_load.py 1 model.pkl test_dataset.tsv histone_mark_name
```


