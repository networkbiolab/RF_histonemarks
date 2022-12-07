import sys
import pandas as pd

data = pd.read_csv(sys.argv[1],sep = "\t")

div = len(data)/5
print(div)

print("0 "+str(int(div)))
print(str(int(div))+" "+str(int(div)*2))
print(str(int(div)*2)+" "+str(int(div)*3))
print(str(int(div)*3)+" "+str(int(div)*4))
print(str(int(div)*4)+" "+str(len(data)))


p1 = data.iloc[0:int(div)]
p2 = data.iloc[int(div):int(div)*2]
p3 = data.iloc[int(div)*2:int(div)*3]
p4 = data.iloc[int(div)*3:int(div)*4]
p5 = data.iloc[int(div)*4:len(data)]

p1.to_csv("dataset_p1.txt",index=False, sep="\t")
p2.to_csv("dataset_p2.txt",index=False, sep="\t")
p3.to_csv("dataset_p3.txt",index=False, sep="\t")
p4.to_csv("dataset_p4.txt",index=False, sep="\t")
p5.to_csv("dataset_p5.txt",index=False, sep="\t")
