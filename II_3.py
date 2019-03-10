import numpy as np
import sys

file = open(sys.argv[1]+".txt.conll","r")
Xfile = open(sys.argv[1]+".txt.pos.lima","w")


lignes = file.readlines()
for i in range(len(lignes)):
	lignes[i] = lignes[i].split('\t')

for i in range(len(lignes)):
	if len(lignes[i]) >= 4:
		mots = lignes[i][1].split(' ')
		for mot in mots:
			Xfile.write(mot+"_"+lignes[i][4]+" ")