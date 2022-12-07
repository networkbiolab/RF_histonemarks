import sys
import pandas as pd

data_1 = pd.read_csv(sys.argv[1],sep = "\t")
data_2 = pd.read_csv(sys.argv[2],sep = "\t")
data_3 = pd.read_csv(sys.argv[3],sep = "\t")
data_4 = pd.read_csv(sys.argv[4],sep = "\t")

data_1 = pd.concat([data_1,data_2])
data_1 = pd.concat([data_1,data_3])
data_1 = pd.concat([data_1,data_4])

data_1.index = range(data_1.shape[0])

#print(data_1)

name = sys.argv[1][:-4]+"_"+sys.argv[2][8:-4]+"_"+sys.argv[3][8:-4]+"_"+sys.argv[4][8:-1]+"t"
print(name)

data_1.to_csv(name,index=False, sep="\t")
