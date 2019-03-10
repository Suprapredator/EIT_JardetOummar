import sys

def transfert():
	texte_base = open("wsj_0010_sample.txt.pos.stanford", "r")
	etiquettes = open("POSTags_PTB_Universal.txt", "r", encoding="utf16", errors='ignore')
	texte_out = open("wsj_0010_sample.txt.pos.univ.standford", "w+")

	tab_etiquettes = etiquettes.readlines()

	true_tab = []
	for duo_etiquette in tab_etiquettes:
		true_tab.append(duo_etiquette.split())
		
	string_base = texte_base.read()

	for duo in reversed(true_tab):
		string_base = string_base.replace(duo[0], duo[1])

	texte_out.write(string_base)


if __name__ == '__main__':
	transfert()