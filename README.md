# Random Forest for the identification of relationships between epigenetic marks and its application to robust assignment of chromatin states
This approach is implemented in Python 3.7. Please follow specific instructions for your platform to install the Python 3 interpreter [here](https://www.python.org/downloads/).
## Requirements
- scikit-learn == 0.24.2
- numpy ==  1.19.5
- pandas == 1.1.2
- scipy == 1.5.4
- joblib == 1.0.0
# Dataset creation
For the dataset creation, it is necessary to have all ChIP-seq data in Bedgraph format. The dataset will be created by chromosome. For this, we use the script extract_chr.py to divide our data.
```
python3 extract_chr.py -I input_file.bedgraph -C chromosome
```

The second step is to use the script dataset_bedgraph.py to convert the data to a table that is divided into fragments of *n* bases of size. In this study, we use an *n* value of 2000.
```
python3 dataset_bedgraph.py -I input_file_1.bedgraph input_file_2.bedgraph ... input_file_n.bedgraph -W n_size(int)
```

Then, our approach considers fragments upstream and downstream of the site which we want to predict. For this, the script datasets_distance_parallel.py was used. This script needs as input arguments the output file of dataset_bedgraph.py, the number of bases to consider upstream and downstream, the size of fragments (same number used in the previous script), and the number of cores to use (this script allows to parallelize the task). In this work, a distance value of 10000 bases was used.
```
python3 datasets_distance_parallel.py output_dataset_bedgraph_file.tsv distance(int) fragment_size(int) n_cores(int)
```

To extract the attributes or a subset of features of our generated dataset and generate the labels of the histone marks to train the Random Forest. The script mega_subset_bedgraph.py can help us. This script use as input arguments the file of the datasets from which we want to extract the data, a file with the name of attributes and the label of the histone mark to predict, the name of the output file, the distance upstream and downstream and fragment size used to create the dataset.
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
The next step is to use the created dataset to train and test the Random Forest regressor algorithms. For this, we use the script RF_regression_load.py. This script has two options for usage, the first (0) uses the entire dataset to train the algorithms, and the second (1) loads a model and tests it with the given dataset. The output of this script is the trained model in format .pkl and the importance values of the attributes used. The input arguments of the script using the first option (0) are the dataset file, the number of trees, depth (0 to max depth), the number of cores, and the name of the histone mark to predict.
```
python3 RF_regression_load.py 0 dataset.tsv n_trees(int) depth(int) n_cores(int) histone_mark_name
```
The input arguments of the second option (1) are the model to test in .pkl format, the dataset to test, and the predicted histone mark.
```
python3 RF_regression_load.py 1 model.pkl test_dataset.tsv histone_mark_name
```

## Using a model pre trained to predict histone mark
Once a model is trained, we can generate a prediction without retraining. For this, we will use the .pkl files generated in the training stage and through the predict.py script. As input arguments, this script needs the .pkl file with the previously trained model, the dataset to use, and the name of the histone mark to predict.
```
python3 predict.py model.pkl dataset.tsv histone_mark_name > prediction.txt
```

# Chromatin states predictor
As our Random Forest approach generates files in BEDgraph format, it was impossible to directly use [CHROMHMM](https://www.nature.com/articles/nmeth.1906), so a chromatin state predictor was performed using the mappings defined by CHROMHMM as labels in our training dataset. These tags were assigned using the BAM files of histone marks obtained from ChIP-seq experiments and a fragment size equal to that used to generate the predictions (see REF).
To generate these models of chromatin states, Random Forest models of the classification type will be trained using data from a single chromosome (in this study, chromosome 1). That is why, in the first instance, it is necessary to extract the chromatin states assigned with CHROMHMM (the file used is obtained with the "MakeBrowserFiles" option, see the CHROMHMM [manual](compbio.mit.edu/ChromHMM/ChromHMM_manual.pdf) for more details ) only for the chromosome that we will use in the stage of training. Once these data have been extracted, we will transform these states into binary multi-labels, which will be represented using 0 and 1, representing the absence or presence of the state in the fragment. For this, the script labels.py will be used. This script, as input arguments, uses the chromosome state file and the chromosome size.
```
python3 labels.py chromatin_states_chr.txt chr_size(int) > labels_chr.txt
```

Then using histone mark data in the format generated by the dataset_bedgraph.py script, merging this file with the one generated with labels.py is necessary. For this task, we will use the *paste* command.
```
paste histone_marks_chr.txt labels_chr.txt > dataset_pred_states.txt
```

The next step is to use this generated dataset to train our model. The first step will be to divide this dataset into five files because we will generate five models to predict information from a chromosome. This is done as cross-validation to avoid using the same training data in the testing stage and thus not cause a possible overfitting of the model. To split our dataset, we will use the div.py script. This script needs only the file of our dataset as arguments.
```
python3 div.py dataset_pred_states.txt
```
Then to train our models, we will need to join the files generated with the previous script, leaving out the fragment file we will use for testing. We will do this with the join.py script, which takes four of the five files generated with div.py as input arguments.
```
python3 join.py dataset_p1.txt dataset_p2.txt dataset_p3.txt dataset_p4.txt
```

Finally, using the files generated above, we will train and test our Random Forest classifier models through the multiLabel_RF_clf_CV.py script. This script needs as input arguments the dataset file generated with join.py, the number of trees to use in the Random Forest algorithm, the depth of trees to use, the fragment dataset to test (files obtained with div.py), and the name of the model to generate.
```
python3 multiLabel_RF_clf_CV.py dataset_p1_p2_p3_p4.txt n_trees(int) 15 dataset_p5.txt pred_p5_
```

## Using a model pre trained to predict Chromatin states
To use a pre-trained chromatin state assignment model. It is possible to use the script predict_chrStates.py. The input arguments are the .pkl file of the model to use, the file of the chromosome segment to predict (for example, the file obtained with div.py), and the output file header.
```
python3 predict_chrStates.py model_chrStates.pkl dataset_p1.txt States > States_predicted.txt
````



