from lxml import etree
import numpy as np

def transformer():
	lima_res = open("test2.txt", "r")
	stdfd_res = open("stdfd.output.txt", "r")

	lima_out = open ("lima.txt", "w")
	stdfd_out = open ("stdfd.txt", "w")

	# etiquettes
	fichier_etiquette = open("correspondance_ner.txt")
	etiquettes = fichier_etiquette.readlines();

	eti_lima = []
	eti_std = []
	for elem in etiquettes:
		eti_lima.append(elem.split()[0])
		if (len(elem.split()) > 1):
			eti_std.append(elem.split()[1])

	# on fait en sorte que le curseur passe les 2 premières lignes du fichier de standford
	# car elles ne contiennent aucune info utile
	stdfd_res.readline()
	stdfd_res.readline()

	# ecriture standford
	for line in stdfd_res.readlines():
		entity_line = line.split()
		i = 0
		entity = []
		while entity_line[i] not in eti_std:
			entity.append(entity_line[i])
			i = i + 1
		tag = entity_line[i]
		
		for elem in entity:
			stdfd_out.write(elem+"_"+tag+" ")

	# ecriture lima
	for line in lima_res.readlines():
		entity_line = line.split()
		i = 0
		entity = []
		while entity_line[i] not in eti_lima:
			entity.append(entity_line[i])
			i = i + 1
		tag = entity_line[i]
		if tag == "Numex.NUMBER":
			continue
		
		for elem in entity:
			lima_out.write(elem+"_"+tag+" ")




if __name__ == '__main__':
	transformer()
