from lxml import etree
import numpy as np
import sys

tree = etree.parse(sys.argv[1])
root = tree.getroot()

entities = []
for manitou in root:
	entity = []
	for i in range(len(manitou)):
		entity.append(manitou[i].text)
	entities.append(entity)

numpyEntities = np.array(entities)

lignes = []
entitesVues = []

for i in range(0,len(numpyEntities)):
	if (not (numpyEntities[i,0] in entitesVues)):
		entitesVues.append(numpyEntities[i,0])
		ligne = list()
		ligne.append(numpyEntities[i,0])
		ligne.append(numpyEntities[i,3])
		nbOcc = np.count_nonzero(numpyEntities[:,0]==ligne[0])
		ligne.append(str(nbOcc))
		ligne.append(str(int(nbOcc*100/len(numpyEntities)))+"%")
		lignes.append(ligne)

file = open("lima.output.txt","w")

for ligne in lignes:
	writing_ligne = ligne[0]+"\t"+ligne[1]+"\t"+ligne[2]+"\t"+ligne[3]+"\n"
	file.write(writing_ligne)
