import numpy as np
import sys

file = open("Ressources/"+sys.argv[2],"r")
Xfile = open("Ressources/"+sys.argv[3],"w")
mode = sys.argv[1]

lignes = file.readlines()
for i in range(len(lignes)):
    lignes[i] = lignes[i].split('</ENAMEX>')

tab = []
for ligne in lignes:
    for subLigne in ligne:
        if "<ENAMEX" in subLigne :
            tab.append(subLigne.split('<ENAMEX ')[1])

res = []
for word in tab:
    buff = word.split('>')
    buff[0] = buff[0].split('="')
    if mode == "lima" or " " not in buff[1]:
        res.append([buff[1],buff[0][1][:-1]])
    else:
        composedWord = buff[1].split(' ')
        for w in composedWord:
            res.append([w,buff[0][1][:-1]])

text = ""
for word in res:
    text += word[0]+"_"+word[1]+" "

Xfile.write(text[:-1])

