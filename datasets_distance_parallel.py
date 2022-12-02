import sys
import pandas as pd
import multiprocessing as mp
import os

#d: distancia rio arriba y rio abajo (nt)
d = sys.argv[2]
#frag: tamano de los fragmentos de los datasets
frag = sys.argv[3]
#w: numero de fragmentos rio arriba y rio abajo
w = int(d)/int(frag)
w = int(w)
#n_proc: numero de procesadores
n_proc = sys.argv[4]

#se crea el primer archivo el cual contedra el header del archivo final
f = pd.read_csv(sys.argv[1],sep="\t")
with open("header.txt",'w') as out:
    for i in range(0,w+1):
        for j in range(0,len(list(f))-1):
            out.write(list(f)[j]+"_-"+str(w-i)+"\t")
    for i in range(1,w+1):
        for j in range(0,len(list(f))-1):
            out.write(list(f)[j]+"_"+str(i)+"\t")
    out.write(list(f)[-1]+"\n")



#Funcion que crea el dataset
def dataset(tuple):
	a = int(tuple[0])
	b = int(tuple[1])
	c = int(tuple[2])
	proc = tuple[3]
	#print("tupla",tuple)
	if b == 0:
		x = b+a
	if b-a >= 0 and b+a < len(f):
		x=b
	#print("x-a:",x-a," x+a:",x+a)
	with open(str(proc)+"dataset.txt",'w') as file:
		while(x < c and x+a < len(f)):
			for y in range(x-a,x+a+1):
				for z in range(0,len(f.iloc[y].tolist()[:-1])):
					file.write(str(f.iloc[y].tolist()[z])+"\t") #n histonas en la pos y
			file.write(str(f.iloc[x].tolist()[-1])+"\n") #label
			x+=1 #siguiente posicion

def test(tuple):
	a = tuple[0]
	b = tuple[1]
	c = tuple[2]
	d = tuple[3]
	print("a ",a,"b ",b,"c ",c,"d ",d)

#creacion tuplas
i = 0
p = 1
tup = []
while(i < len(f)):
	if p != int(n_proc):
		#print(p,">>>",n_proc)
		i_0 = i
		i+=len(f)/int(n_proc)
		tup = tup+[(w,i_0,i,p),]
		p+=1
	else:
		i_0 = i
		tup = tup+[(w,i_0,len(f),p),]
		i = len(f)

def cube(x):
    return x**3

aux1 = tuple((40,0,56,1))
aux2 = tuple((40,56,112,2))
aux3 = zip(aux1,aux2)

#print(tup)
#print(len(f))
with mp.Pool(processes=int(sys.argv[4])) as pool:
   	#results = pool.map(cube, range(1,int(sys.argv[4])+1))
	#results = pool.map(dataset,aux3)
	#results = pool.map(test,[(40,0,56,1),(40,56,112,2)])
	#results = pool.map(dataset,tup)
	pool.map(dataset,tup)
	#pool.map(dataset,[(40,0,56.0,1),(40,56.0,112.0,2),(40,112.0,168,3)])
#	pool.map(dataset,[(40,0,56.0,1),(40,56.0,112.0,2)])
#print(results)

n_out = ""

for k in range(0,len(list(f))-1):
	n_out += list(f)[k]+"_"
n_out += "label_"+list(f)[-1]

n_files = "header.txt\t"
for t in range(1,int(sys.argv[4])+1):
	if t == int(sys.argv[4]):
		n_files += str(t)+"dataset.txt"
	else:
		n_files += str(t)+"dataset.txt"+"\t"
os.system("cat "+n_files+" > dataset_"+frag+"_"+d+".txt")
os.system("rm "+n_files )


