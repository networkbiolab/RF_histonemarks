import sys
import numpy as np

with open(sys.argv[1],'r') as file:
	data = file.readlines()

chr1 = np.zeros(int(sys.argv[2]),dtype=int)

#chr2 = np.zeros(242193529,dtype=int)

for line in data:
	line = line[:-1]
	sp_line = line.split("\t")
	for i in range(int(sp_line[1]),int(sp_line[2])):
		chr1[i] = sp_line[3].replace("E","")


print("States_label")
frag = 2000
for j in range(0,len(chr1),frag):
	states = np.zeros(8,dtype=int)
	if (j+frag) <= len(chr1):
		for i in range(j,(j+frag)):
			if chr1[i] != 0:
				states[chr1[i]-1] += 1
		for y in range(0,len(states)):
			if y != len(states)-1:
				#print(round((states[y]/frag)*100),end=",")
				print(round((states[y]/frag)),end=",")
			else:
				#print(round((states[y]/frag)*100))
				print(round((states[y]/frag)))
