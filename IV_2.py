

import sys
from collections import Counter

def getPart(word, part):
	return word.split("/")[part]

def affichage(fichier_in, fichier_out):

	texte_base = open(fichier_in, "r")
	tab = open(fichier_out, "w")

	allWordsTagged = []

	lines = texte_base.readlines()
	for line in lines:
		line = line.split()
		allWordsTagged.extend(line)

	# a partir de la, on a une liste de tous les mots colles a leur tag.
	
	namedEntities = []
	i = 0
	curEntity = ''
	while i < (len(allWordsTagged) - 1):
		curWord = allWordsTagged[i]
		tag = getPart(curWord, 1)
		if(tag == 'O'):
			i = i+1;
		else:
			curEntity = getPart(curWord, 0)
			j = i + 1
			if (j < len(allWordsTagged)):
				nextWord = allWordsTagged[j]

				while (tag == getPart(nextWord, 1)):
					curEntity = curEntity + " " +getPart(nextWord, 0)
					if (j < (len(allWordsTagged) - 1)):
						j = j + 1
						nextWord = allWordsTagged[j]
					else:
						break
			curEntity = curEntity +"/"+tag
			namedEntities.append(curEntity)
			curEntity = ''
			i = j


	entityCounter = Counter(namedEntities)

	namedEntitiesWithNumber = []
	for elem in namedEntities:
		if (not elem in namedEntitiesWithNumber):
			namedEntitiesWithNumber.append(elem +"/"+str(entityCounter[elem]))

	tabEntities = []
	for elem in set(namedEntitiesWithNumber):
		tabEntities.append(elem.split('/'))

	tab.write('{:<40s}{:>15s}{:>25s}{:>38s}'.format("Entité nommée","Type","Nombre d’occurrences","Proportion dans le texte (%)\n\n"))
	for ent in tabEntities:

		tab.write('{:<40s}{:>15s}{:>25s}{:>30.2f}'.format(ent[0], ent[1], ent[2], int(ent[2])/sum(entityCounter.values()))+" ("+ent[2]+"/"+str(sum(entityCounter.values()))+")\n")

if __name__ == '__main__':
	affichage(sys.argv[1], sys.argv[2])