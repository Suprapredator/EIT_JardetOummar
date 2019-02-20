

import sys

def transfert(fichier_in, fichier_out):
	texte_base = open(fichier_in, "r")
	etiquettes = open("POSTags_PTB_Universal.txt", "rb")
	texte_out = open(fichier_out, "w")

	tab_etiquettes = etiquettes.readlines()
	for duo_etiquette in tab_etiquettes:
		duo_etiquette.split()

	string_base = texte_base.read()

	for duo in reversed(duo_etiquette):
		texte_out.write(string_base.replace(duo[0], duo[1]))

if __name__ == '__main__':
	transfert(sys.argv[0], sys.argv[1])