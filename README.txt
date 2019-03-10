Vous trouverez dans ce dossier les scripts ayant servis pour la réalisation du projet:
II_2.py et II_2_conll.py
II_3.py
II_4.py
IV_2.py
transfert_etiquettes.py
V_lima2std.py
V_transfo_pour_evaluate.py
V_translate_reference.py

Dans le dossier Ressources, vous trouverez l’ensemble des fichiers servant pour le projet, ils ont majoritairement été fournis.

Exécution des scripts:

II_2.py: python II_2.py fichier.xml
Parse un xml  de LIMA pour le mettre sous la forme [Entité nommée, Type, Nombre d’occurrences, Proportion dans le texte (%)]

II_2_conll.py: python II_2_conll.py nomFichier
Parse un .conll de LIMA pour le mettre sous la forme Entité nommée_Type

II_3.py: python II_3.py nomFichier
Parse un .conll de LIMA pour le mettre sous la forme mot_etiquette

II_4.py: python II_4.py nomFichierEntrant.extention nomFichierSortie.extention2
Traduit toutes les étiquettes en étiquettes universelles afin que le fichier de LIMA soit compatible avec evaluate.py.

IV_2.py: python IV_2.py nomFicherEntrée nomFicherSortie
Transforme la sortie de l’analyse d’entités nommées de Standford en un tableau de la forme
[Entité nommée, Type, Nombre d’occurrences, Proportion dans le texte, (%)]

V_lima2std.py : nomFichierSortie
Remplace les étiquettes dans la sortie de l’analyse d’entités nommées de LIMA en étiquettes du format de Standford

V_stdout2evaluate.py : ce script sert à l’évaluation et ne s’execute pas

V_transfo_pour_evaluate.py : 
Transforme les sorties des analyses des entités nommées de LIMA et Standford en textes évaluables par le script evaluate.py

V_translate_reference.py :  python V_translate_reference.py option nomFicherEntrée nomFicherSortie
Ce script traduit un texte ayant des balises “ENAMEX” afin de le préparer pour evaluate.py.
Le paramètre “option” peut prendre la valeur “lima” afin que le texte soit mis sous la forme entiteNommee_type en respectant les mots composés (motEspaceMot_type). Si la valeur est différente de “lima” alors la traduction se fait comme pour Stanford.

