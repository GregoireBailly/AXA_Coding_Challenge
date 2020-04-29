class Person:
    def __init__(self, name, domain, morning, evening):
        self.name = name
        self.domain = domain
        self.morning  = morning
        self.evening = evening

    def __str__(self):
        toPrint = self.name
        toPrint += str(self.domain)
        toPrint += str(self.morning)
        toPrint += str(self.evening)
        return toPrint

#Prends le nom d'un fichier en entrée et renvoie l'objet
def lecture_fichier(nom_fichier):
    import json
    with open(nom_fichier) as json_file:
        data = json.load(json_file)
        #print(data)
        quotas = []
        indice_quotas = []
        personnes = []
        for i in data["quotas"]:
            quotas.append(data["quotas"][i])
            indice_quotas.append(i)
        d = data["workers"]
        for i in d:
            #print(d[i])
            nom = i
            domain = indice_quotas.index(d[i]["domain"])
            morning = d[i]['morningOptions']
            evening = d[i]['eveningOptions']
            p = Person(nom, domain, morning, evening)
            #print(p)
            personnes.append(p)
        return quotas, personnes

print(lecture_fichier('Inputs/input_1.json'))
