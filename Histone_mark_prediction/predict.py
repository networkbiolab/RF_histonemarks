import sys
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor
import joblib

rf = joblib.load(sys.argv[1])
name_label = sys.argv[3]+"_label"
features = pd.read_csv(sys.argv[2],sep='\t')

# Label that I want to predict
labels = np.array(features[name_label])

# Remove the labels from the features
features = features.drop(name_label, axis=1);

# Saving feature names for later use
feature_list = list(features.columns)

# Convert to numpy array
features = np.array(features)

predictions = rf.predict(features)


distance = 10000
fragment = 2000
div = distance/fragment
start = 0
end = fragment

print(sys.argv[3])
for j in range(int(div)):
	print("0")
	start+=fragment
	end+=fragment
for i in predictions:
	print(i)
	start+=fragment
	end+=fragment
for k in range(int(div)):
	print("0")
	start+=fragment
	end+=fragment

