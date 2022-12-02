import argparse
from collections import defaultdict

parser = argparse.ArgumentParser()
parser.add_argument("-I","--inputFile",help="Bed files",required=True,type=str)
parser.add_argument("-C","--chr",help="chromosome")
args = parser.parse_args()

D = defaultdict(list)
with open(args.inputFile,'r') as f:
    data = f.readlines()
    for line in data:
        line = line[:-1]
        sp_line = line.split("\t")
        D[sp_line[0]].append(line)

sp_file = args.inputFile.split(".")
file = open(args.chr+"_"+sp_file[0]+".bed",'w')
for i in range(len(D[args.chr])):
	file.write(D[args.chr][i]+"\n")
file.close()
