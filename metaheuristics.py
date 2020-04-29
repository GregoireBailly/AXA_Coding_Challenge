from Person import *
from utils import *
from parser import *

import random
from copy import deepcopy

pop = None
quotas = None

#main function for tabu search opti
def TSopti(apop, aquotas):
    global pop
    global quotas
    pop = apop
    quotas = aquotas

    #params
    listLen = 30
    neighbourhoodSize = 50
    convergence = 30

    timeSinceLastBestUpdate = 0

    sol, personW = generateRanValidSol()

    print(solIsOkPerson(sol))
    print(getValidityScore(personW))
    fillPop(sol)
    return pop



def generateRanValidSol():
    sol = []
    personWorking = []

    solLen = 0
    for person in pop:
        solsForP = []
        for mOption in person.morning:
            for eOption in person.evening:
                solsForP.append(False)
                solLen += 1
        sol.append(solsForP)
        personWorking.append(False)

    while (getValidityScore(personWorking) != 0):
        personIndex = random.randint(0, len(sol)-1)

        if personWorking[personIndex]: continue
        personWorking[personIndex] = True

        optionIndex = random.randint(0, len(sol[personIndex])-1)

        #print(str(personIndex) + " "+str(optionIndex))
        #print("--"+str(len(sol[personIndex])))
        sol[personIndex][optionIndex] = True

    return sol, personWorking
    

#check that one person isn't used more than once
def solIsOkPerson(sol):
    for person in sol:
        if personIsOk(person) == False:
            return False
        
    return True

def personIsOk(person):
    appearing = 0
    for option in person:
        if option: appearing += 1

    if appearing > 1:
        return False
    else:
        return True


def getValidityScore(personWorking):
    workersByQuota = []
    validityScore = 0
    for i in quotas:
        workersByQuota.append(0)

    for working, person in zip(personWorking, pop):
        if working:
            workersByQuota[person.domain] += 1
    
    for domainQuota, workers in zip(quotas, workersByQuota):
        if workers < domainQuota:
            validityScore += domainQuota - workers
    
    return validityScore


def fillPop(sol):
    for personS, personP in zip(sol, pop):
        option_index = 0
        for opt in personS:
            if opt: break
            option_index += 1

        
        personP.mOption = int(option_index / len(personP.evening))
        personP.eOption = option_index%len(personP.evening)


if __name__ == "__main__":
    n = 2
    url = "Inputs/input_" + str(n) + ".json"

    aquotas, apop = lecture_fichier(url)

    finalSol = TSopti(apop, aquotas)


    score = score(finalSol, aquotas)
    print ("done, score = "+ str(score))


