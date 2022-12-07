import sys
import pandas as pd
import re

#INPUT
#ARGV[1] txt con el dataset
#ARGV[2] txt con las columnas a extraer
#ARGV[3] archivo output
#ARGV[4] d
#ARGV[5] frag

d = sys.argv[4]
frag = sys.argv[5]

w = int(d)/int(frag)
w = int(w)

data = pd.read_csv(sys.argv[1], sep="\t")

with open(sys.argv[2],'r') as file:
	lines = file.readlines()

aux = []
x = ''
y = ''
for line in lines:
	line = line[:-1]
	if re.search('label',line):
		sp_line = line.split("_")
		x = sp_line[0]+"_-0"
		y = line
		aux.append(x)
	else:
		for i in range(0,w+1):
			aux.append(line+"_-"+str(w-i))
		for j in range(1,w+1):
			aux.append(line+"_"+str(j))

df_nuevo = data[aux].copy()
df_nuevo = df_nuevo.rename(columns={x:y})
df_nuevo.loc[(df_nuevo[y] < 2), y] = df_nuevo[y]/2
df_nuevo.loc[(df_nuevo[y] >= 2), y] = 1
df_nuevo.to_csv(sys.argv[3],index=False, sep="\t")
