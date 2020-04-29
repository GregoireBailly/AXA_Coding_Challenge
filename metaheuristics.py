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
    neighbourhoodSize = 15
    convergence = 100

    timeSinceLastBestUpdate = 0

    sol, personW = generateRanValidSol()
    bSol = deepcopy(sol)
    print("begin sol Ok Person: " + str(solIsOkPerson(sol)))

    fillPop(sol)

    b_score = score(pop,quotas)
    print("start score: ", b_score)

    while timeSinceLastBestUpdate <= convergence:
        timeSinceLastBestUpdate += 1

        bestN = genNeighbour(sol)

        fillPop(bestN)
        bestN_score = score(pop, quotas)

        for i in range(neighbourhoodSize):
            n = genNeighbour(sol)
            fillPop(n)
            n_score =score(pop, quotas)

            if n_score<=bestN_score:
                bestN = deepcopy(n)
                bestN_score = n_score
            
        sol = deepcopy(bestN)


        if bestN_score < b_score:
            print("new best sol, score: ", bestN_score)
            bSol = deepcopy(sol)
            b_score = bestN_score
            timeSinceLastBestUpdate = 0
        
        timeSinceLastBestUpdate +=1
             

    print("end sol Ok Person: " + str(solIsOkPerson(sol)))
    print("end sol validityscore: " + str(getValidityScore(personW)))
    fillPop(bSol)
    return pop

def countPersonWorking(personWorking):
    count = 0
    for p in personWorking:
        if p: count +=1
    return count

def genNeighbour(sol):
    n = deepcopy(sol)
    personWorking = []
    indexes = []
    for person in n:
        personWorking.append(False)
        for option in person:
            if option:
                lastIndexofP = len(personWorking)-1
                indexes.append(lastIndexofP)
                personWorking[lastIndexofP] = True
                break

    #print("before: ", countPersonWorking(personWorking))

    #from the working people randomly select one
    randIndex = random.randint(0, len(indexes)-1)
    randP = indexes[randIndex]
    for option in n[randP]:
        option = False
    
    if personWorking[randP] == False: print("Error 1X in neighbour gen")
    personWorking[randP] = False
    
    #print("middle: ", countPersonWorking(personWorking))

    if getValidityScore(personWorking) == 0 :
        return n
    
    #find someone from the same domain and add him
    domain_toFill = pop[randP].domain

    P_sameDom_Indexes = []
    j = 0
    for person in pop:
        if person.domain == domain_toFill and personWorking[j]==False:
            P_sameDom_Indexes.append(j)
        j += 1
    
    randI = random.randint(0, len(P_sameDom_Indexes)-1)
    randP = P_sameDom_Indexes[randI]

    personWorking[randP] = True
    #print("after: ", countPersonWorking(personWorking))
    if getValidityScore(personWorking) != 0 :
        print("Error (X2) in neighbour gen")

    randO = random.randint(0, len(n[randP])-1)
    n[randP][randO] = True

    return n


    


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

    #print("score begin of gen " + str(getValidityScore(personWorking)))
    #print("ok : "+str(solIsOkPerson(sol)))

    while (getValidityScore(personWorking) != 0):
        personIndex = random.randint(0, len(sol)-1)

        if personWorking[personIndex]: continue
        personWorking[personIndex] = True

        optionIndex = random.randint(0, len(sol[personIndex])-1)

        #print(str(personIndex) + " "+str(optionIndex))
        #print("--"+str(len(sol[personIndex])))
        sol[personIndex][optionIndex] = True

    #print("score end of gen " + str(getValidityScore(personWorking)))
    #print("ok : "+str(solIsOkPerson(sol)))
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
    count = 0
    for personS, personP in zip(sol, pop):
        option_index = 0
        working = False
        for opt in personS:
            if opt: 
                working = True
                break
            option_index += 1

        if working:
            count+=1
            personP.optionM = int(option_index / len(personP.evening))
            personP.optionE = option_index%len(personP.evening)
        else:
            personP.optionM = -1
            personP.optionE = -1

    #print("spotted worker: "+ str(count))


if __name__ == "__main__":
    n = 2
    url = "Inputs/input_" + str(n) + ".json"

    aquotas, apop = lecture_fichier(url)

    finalSol = TSopti(apop, aquotas)

    score = score(finalSol, aquotas)


    nbP = 0
    for p in finalSol:
        if p.optionM != -1:
            nbP +=1

    print("end nb Personne ",nbP)
    print ("done, score = "+ str(score))


