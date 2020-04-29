from Person import *

def score(solution, quotas):
    #check if the solution is valid
    if isValid(solution, quotas) == False:
        return float("inf")
        
    Mtransports = dict()
    Etransports = dict()
    for person in solution:
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

def isValid(solution, quotas):
    workersByQuota = []
    for i in quotas:
        workersByQuota.append(0)

    for person in solution:
        if person.optionM != -1:
            workersByQuota[person.domain] += 1
    
    for domainQuota, workers in quotas, workersByQuota:
        if workers < domainQuota:
            return False

    return True

