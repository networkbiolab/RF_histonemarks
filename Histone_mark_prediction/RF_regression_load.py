import sys
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# Using Skicit-learn to split data into training and testing sets
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix
#from sklearn.ensemble import RandomForestClassifier
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

if sys.argv[1] == "0":
	# Read the data
	print("==Reading file==")
	features = pd.read_csv(sys.argv[2],sep='\t')
	name_label = sys.argv[6]+"_label"
	# Label that I want to predict
	labels = np.array(features[name_label])
	# Remove the labels from the features
	features = features.drop(name_label, axis=1);
	# Saving feature names for later use
	feature_list = list(features.columns)

	# Convert to numpy array
	features = np.array(features)


	print("==Instantiate model==")
	# Instantiate model
	if int(sys.argv[4]) != 0:
		print("rf = RandomForestRegressor(n_estimators = ",int(sys.argv[3]),", random_state = 0, n_jobs = ",int(sys.argv[5]),", max_depth = ",int(sys.argv[4]),")")
		rf = RandomForestRegressor(n_estimators = int(sys.argv[3]), random_state = 0, n_jobs = int(sys.argv[5]), max_depth = int(sys.argv[4]))
	else:
		print("rf = RandomForestRegressor(n_estimators = ",int(sys.argv[3]),", random_state = 0, n_jobs = ",int(sys.argv[5]),")")
		rf = RandomForestRegressor(n_estimators = int(sys.argv[3]), random_state = 0, n_jobs = int(sys.argv[5]))

	print("==Train model==")
	# Train the model on training data
	rf.fit(features, labels)

	print("==Saving model==")
	joblib.dump(rf, 'modelo_RF_entrenado_trees'+sys.argv[3]+'depth'+sys.argv[4]+'.pkl',compress=3) # Guardo el modelo.


	print('\n')

	importances = list(rf.feature_importances_)
	feature_importances = [(feature, round(importance, 5)) for feature, importance in zip(feature_list, importances)]
	feature_importances = sorted(feature_importances, key = lambda x:x[1], reverse = True)

	print()
	[print('Variable: {:20} Importance: {}'.format(*pair)) for pair in feature_importances];

if sys.argv[1] == "1":
	rf = joblib.load(sys.argv[2])
	name_label = sys.argv[4]+"_label"
	features = pd.read_csv(sys.argv[3],sep='\t')

	# Label that I want to predict
	labels = np.array(features[name_label])

	# Remove the labels from the features
	features = features.drop(name_label, axis=1);

	# Saving feature names for later use
	feature_list = list(features.columns)

	# Convert to numpy array
	features = np.array(features)

	predictions = rf.predict(features)

	test_score = r2_score(labels,predictions)
	spearman = spearmanr(labels,predictions)
	pearson = pearsonr(labels,predictions)

	print("R2: ",test_score)
	print("Spearman: ",spearman)
	print("Pearson: ",pearson)
