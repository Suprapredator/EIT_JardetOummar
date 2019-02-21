import numpy as np
import sys

dico_universel = open("Ressources/dictionnaire.txt", "r")
file = open(sys.argv[1],"r")
Xfile = open(sys.argv[2],"w")

lignes = file.readlines()
lignes_univ = dico_universel.readlines()
for i in range(len(lignes_univ)):
    lignes_univ[i] = lignes_univ[i].replace('\n','')
    lignes_univ[i] = lignes_univ[i].split(' ')


for i in range(len(lignes)):
    lignes[i] = lignes[i].split(' ')
    for j in range(len(lignes[i])):
        lignes[i][j] = lignes[i][j].split('_')

for i in range(len(lignes)):
    for j in range(len(lignes[i])):
        for k in range(len(lignes_univ)):
            if(lignes[i][j][1] == lignes_univ[k][0]):
                lignes[i][j][1] = lignes_univ[k][1]

text = ""
for i in range(len(lignes)):
    for j in range(len(lignes[i])):
        print(lignes[i][j][0]+"_"+lignes[i][j][1])
        text += lignes[i][j][0]+"_"+lignes[i][j][1]+" "
    text = text[:len(text)]+"\n"

Xfile.write(text)