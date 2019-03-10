from lxml import etree
import numpy as np
import sys

file = open(sys.argv[1]+".txt.conll","r")
Xfile = open(sys.argv[1]+".txt.namedEntity","w")

lignes = file.readlines()
for i in range(len(lignes)):
	lignes[i] = lignes[i].split('\t')

for i in range(len(lignes)):
    if len(lignes[i]) >= 4:
        if lignes[i][5] == 'Location.LOCATION' or lignes[i][5] == 'Organization.ORGANIZATION' or lignes[i][5] == 'Person.PERSON':
            Xfile.write(lignes[i][1]+"_"+lignes[i][5]+" ")
