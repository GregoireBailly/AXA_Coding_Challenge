from parser import *
from utils import *

import random
from copy import deepcopy

n = 2
url = "Inputs/input_" + str(n) + ".json"

quota, liste_personne = lecture_fichier(url)

score_minimal = float("inf")
liste_minimal = []

for iteration in range(1):
    for p in liste_personne:
        p.optionM = random.randint(0, len(p.morning)-1)
        p.optionE = random.randint(0, len(p.evening)-1)
    score_ici = score(liste_personne)
    if score_ici < score_minimal:
        score_minimal = score_ici
        liste_minimal = deepcopy(liste_personne)

print(score_minimal)

creation_json_sortie(liste_minimal)
