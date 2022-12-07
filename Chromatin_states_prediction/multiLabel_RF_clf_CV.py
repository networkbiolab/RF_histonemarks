import sys
import pandas as pd
import numpy as np
from numpy import array, hstack, math
from sklearn.ensemble import RandomForestClassifier
from sklearn.multioutput import MultiOutputClassifier
from sklearn.model_selection import cross_val_score
from sklearn.metrics import confusion_matrix
from scipy.stats import spearmanr, pearsonr
import joblib

#ARGV[1] : dataset_train
#ARGV[2] : trees
#ARGV[3] : depth
#ARGV[4] : dataset_test
#ARGV[5] : name_output

#TRAIN DATA
# Read the data
print("==Reading file==")
features = pd.read_csv(sys.argv[1],sep='\t')
name_label = "States_label"
# Label that I want to predict
labels = np.array(features[name_label])
# Remove the labels from the features
features = features.drop(name_label, axis=1);
# Saving feature names for later use
feature_list = list(features.columns)

labels_2 = []
for i in labels:
	labels_2.append(list(map(int,i.split(","))))

# Convert to numpy array
features = np.array(features)

#TEST DATA

# Read the data
print("==Reading file==")
features_test = pd.read_csv(sys.argv[4],sep='\t')
# Label that I want to predict
labels_test = np.array(features_test[name_label])
# Remove the labels from the features
features_test = features_test.drop(name_label, axis=1);
# Saving feature names for later use
feature_list_test = list(features_test.columns)

labels_2_test = []
for i in labels_test:
	labels_2_test.append(list(map(int,i.split(","))))

# Convert to numpy array
features_test = np.array(features_test)

if int(sys.argv[3]) != 0:
	model = MultiOutputClassifier(RandomForestClassifier(n_estimators = int(sys.argv[2]), random_state = 0, n_jobs = 20, max_depth = int(sys.argv[3]))).fit(features, labels_2)
else:
	model = MultiOutputClassifier(RandomForestClassifier(n_estimators = int(sys.argv[2]), random_state = 0, n_jobs = 20)).fit(features, labels_2)

joblib.dump(model, sys.argv[5]+'modelo_RF_clf_entrenado_t'+sys.argv[2]+'_d'+sys.argv[3]+'.pkl',compress=3)

ypred = model.predict(features_test)

for j in range(0,8):
        array_test = []
        array_pred = []
        for x in labels_2_test:
                array_test.append(x[j])
        for y in ypred:
                array_pred.append(y[j])
        print("==Confusion_matrix_E_"+str((j+1))+"==")
        tn,fp,fn,tp = confusion_matrix(array_test,array_pred).ravel()
        print("TN: ",tn)
        print("FP: ",fp)
        print("FN: ",fn)
        print("TP: ",tp)

        precision = tp/(tp+fp)
        recall = tp/(tp+fn)
        FPR = fp/(fp+tn)
        print()
        print("Precision: ",precision)
        print("Recall: ",recall)
        print("FPR: ",FPR)
        print()

file =  open(sys.argv[5]+"label_pred_t"+sys.argv[2]+"_d"+sys.argv[3]+".tsv",'w')
file.write("Real\tPredicted\n")
for i in range(0,len(labels_2_test)):
        file.write(str(labels_2_test[i])+"\t"+str(ypred[i])+"\n")

file.close()
