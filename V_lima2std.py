import sys

def remplace_etiquette(fichier_out):
	xml_base = open("wsj_0010_sample.txt.se.xml","r")
	xml_out = open(fichier_out,"w")

	fichier_etiquette = open("correspondance_ner.txt")
	etiquettes = fichier_etiquette.readlines();

	eti_lima = []
	eti_std = []
	for elem in etiquettes:
		eti_lima.append(elem.split()[0])
		eti_std.append(elem.split()[1])

	for line in xml_base.readlines():
		for i in range(0, len(eti_std)):
			line = line.replace(eti_lima[i], eti_std[i])
		xml_out.write(line)

if __name__ == '__main__':
	remplace_etiquette(sys.argv[1])