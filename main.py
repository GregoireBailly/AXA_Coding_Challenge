from parser import *
from utils import *

import random
from copy import deepcopy

alea = 60

for n in range(1, 7):
    n = 1
    print("")
    url = "Inputs/input_" + str(n) + ".json"
    quota, liste_personne = lecture_fichier(url)

    print("Jeu de test", n)
    print("Quotas:", quota)
    print("Nombre de personnes:", len(liste_personne))
    nbquota = [0]*len(quota)
    for p in liste_personne:
        nbquota[p.domain] += 1
    print("Nombre de personne par domaine", nbquota)

    score_minimal = float("inf")
    liste_minimal = []

    liste_tmp = [p.domain for p in sorted(liste_personne, key=lambda x: x.domain)]
    liste_indice = []
    print(liste_tmp)
    for i in range(len(quota)):
        liste_indice.append(liste_tmp.index(i))
    liste_indice.append(len(liste_personne))

    liste_range = []
    for i in range(len(quota)):
        liste_actuelle = range(liste_indice[i], liste_indice[i+1])

    for iteration in range(10000):
        for p in liste_personne:
            p.optionM = random.randint(0, len(p.morning)-1)
            p.optionE = random.randint(0, len(p.evening)-1)
            if random.randint(0, 100) < alea:
                p.optionM = -1
                p.optionE = -1
        score_ici = score(liste_personne, quota)
        if score_ici < score_minimal:
            score_minimal = score_ici
            liste_minimal = deepcopy(liste_personne)

    print(n, score_minimal)

    creation_json_sortie(liste_minimal, n)
    exit()
