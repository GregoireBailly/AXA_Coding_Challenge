from parser import *

n = 1
url = "Inputs/input_" + str(n) + ".json"

quota, liste_personne = lecture_fichier(url)

creation_json_sortie(liste_personne)
