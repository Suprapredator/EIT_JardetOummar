

def makeEvaluable(allWordsTagged, fichier_out):
	out = open (fichier_out, "w")


	for word in allWordsTagged:
		if word.split("/")[1] != "O":
			out.write(word.replace("/", "_")+" ")
	"""entitiesTag = []
	for entity in entities:
		entitiesTag.append(entity.split("/"))

	for entity in entitiesTag:
		for word in entity[0].split():
			out.write(word+"_"+entity[1]+" ")"""