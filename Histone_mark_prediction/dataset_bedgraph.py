import sys
import argparse
import pandas as pd

parser = argparse.ArgumentParser()
parser.add_argument("-I","--inputFile",help="Bed files",required=True,type=str, nargs='+')
parser.add_argument("-W","--window",help="size of the fragment",required=True,type=int)
args = parser.parse_args()

out = {}
df = pd.DataFrame()
label = ""
chr = ""

for i in args.inputFile:
	if i != args.inputFile[-1]:
		name = i[:-4]
	else:
		name = i[:-4]+"_label"
		label = i[:-4]
	array = []
	with open(i,'r') as f:
		data = f.readlines()
	for line in data:
		line = line[:-1]
		sp_line = line.split("\t")
		chr = sp_line[0]
		n_frag = (int(sp_line[2])-int(sp_line[1]))/args.window
		
		for j in range(0,int(n_frag)):
			# ~ print(sp_line[3])
			array.append(sp_line[3])
	df[name] = array


df.to_csv("dataset_chr"+chr+"_f"+str(args.window)+"_"+label+".txt", index = False, sep = "\t")

