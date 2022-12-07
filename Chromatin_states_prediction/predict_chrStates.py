import sys
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# Using Skicit-learn to split data into training and testing sets
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix
#from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.multioutput import MultiOutputClassifier
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import KFold
from sklearn.model_selection import cross_val_score
from sklearn.metrics import recall_score
from sklearn.metrics import r2_score
from scipy.stats import spearmanr, pearsonr

#from sklearn.metrics import plot_roc_curve
from sklearn.metrics import roc_curve, roc_auc_score
#from sklearn.externals import joblib
import joblib

rf = joblib.load(sys.argv[1])
#name_label = sys.argv[3]+"_label"
features = pd.read_csv(sys.argv[2],sep='\t')

# Label that I want to predict
#labels = np.array(features[name_label])

# Remove the labels from the features
#features = features.drop(name_label, axis=1);

# Saving feature names for later use
feature_list = list(features.columns)

# Convert to numpy array
features = np.array(features)

predictions = rf.predict(features)
#print(predictions)

#distance = 10000
#fragment = 2000
#div = distance/fragment
#start = 0
#end = fragment

print(sys.argv[3])
#for j in range(int(div)):
	#print(start,"\t",end,"\t",0)
	#print("0")
#	print("[0 0 0 0 0 0 0 0]")
	#start+=fragment
	#end+=fragment
for i in predictions:
	#print(start,"\t",end,"\t",i)
	print(i)
	#start+=fragment
	#end+=fragment
#for k in range(int(div)):
	#print(start,"\t",end,"\t",0)
	#print("0")
#	print("[0 0 0 0 0 0 0 0]")
	#start+=fragment
	#end+=fragment
#test_score = r2_score(labels,predictions)
#spearman = spearmanr(labels,predictions)
#pearson = pearsonr(labels,predictions)

#print("R2: ",test_score)
#print("Spearman: ",spearman)
#print("Pearson: ",pearson)
