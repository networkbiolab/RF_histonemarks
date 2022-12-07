import sys
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.multioutput import MultiOutputClassifier

#from sklearn.metrics import plot_roc_curve
from sklearn.metrics import roc_curve, roc_auc_score
#from sklearn.externals import joblib
import joblib

rf = joblib.load(sys.argv[1])
features = pd.read_csv(sys.argv[2],sep='\t')


# Saving feature names for later use
feature_list = list(features.columns)

# Convert to numpy array
features = np.array(features)

predictions = rf.predict(features)

print(sys.argv[3])
for i in predictions:
	print(i)
	
