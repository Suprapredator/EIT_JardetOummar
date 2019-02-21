

import sys
from collections import Counter

def affichage(fichier_in, fichier_out):

	texte_base = open(fichier_in, "r")
	tab = open(fichier_out, "w")

	allWordsTagged = []

	lines = texte_base.readlines()
	for line in lines:
		line = line.split()
		allWordsTagged.extend(line)

	# a partir de la, on a une liste de tous les mots colles a leur tag.
	
	namedEntitiesWithNumber = []
	myCounter = Counter(allWordsTagged)
	for word in allWordsTagged:
		if(word.split("/")[1] != 'O'):
			namedEntitiesWithNumber.append(word +"/"+str(myCounter[word]))

	namedEntities = []
	myOtherCounter = Counter(namedEntitiesWithNumber)
	for elem in set(namedEntitiesWithNumber):
		namedEntities.append(elem.split('/'))

	tab.write("Entité nommée\t\tType\t\t\tNombre d’occurrences\t\tProportion dans le texte (%)\n")
	for ent in namedEntities:

		tab.write(ent[0]+"\t\t\t\t"+ent[1]+"\t\t\t"+ent[2]+"\t\t\t\t\t\t\t"+str(int(ent[2])/sum(myOtherCounter.values()))+" ("+ent[2]+"/"+str(sum(myOtherCounter.values()))+")\n")

if __name__ == '__main__':
	affichage(sys.argv[1], sys.argv[2])