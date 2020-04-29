from Person import *

def score(population):
    Mtransports = dict()
    Etransports = dict()
    for person in population:
        #add 1 to the transports used on the morning
        Moption = person.morning[person.optionM]
        
        for transport in Moption:
            t = str(transport)
            if t in Mtransports:
                Mtransports[t] += 1
            else:
                Mtransports[t] = 1

        #add 1 to the transports used on the evening
        Eoption = person.evening[person.optionE]
        
        for transport in Moption:
            t = str(transport)
            if t in Etransports:
                Etransports[t] += 1
            else:
                Etransports[t] = 1

    #compute score from transports dicts
    score = 0
    for passengerNb in Mtransports.values:
        score =+ passengerNb * (passengerNb - 1)

    for passengerNb in Etransports.values:
        score =+ passengerNb * (passengerNb - 1)

    return score
