from numpy.lib.scimath import log10
from math import log
import matplotlib.pyplot as plt

# l = [2, 3, 5, 7, 11, 13, 17, 19, 23, 27, 29]
# len(l)
# s = 0
# for i in l:
#     s += i*(1/log10(29))
# print(s)

# nbreDePremier = 27/(log((27/2)))

# proba = nbreDePremier/l[-1]

# probaTest = len(l)/l[-1]

# erreur = abs(proba - probaTest)
# print(erreur)

def isPremier(x):
    if x == 1:
        return False
    for i in range(2, x//2 + 1):
        if x%i == 0:
            return False
    return True

isPremier(2)
def primeList(x):
    pList = []
    if x == 1 or x == 0:
        return []
    for i in range(2,x):
        if isPremier(i):
            pList += [i]
    return pList

def listFactor(x):
    if x == 1:
        return []
    if isPremier(x):
        return [x]
    for i in primeList(x):
        if x%i == 0:
            return listFactor(int(x/i)) + [i]

def primeDefactoring(x):
    unevenFacto = listFactor(x)
    Factolist = []
    for i in list(set(unevenFacto)):
        Factolist += [(i, unevenFacto.count(i))]
    return Factolist
    
primeDefactoring(100)
listFactor(3)
primeList(10)

def pi(x):
    if x == 1:
        return 0
    if x < 6:
        nbre = piNormal(x)
    elif x < 13:
        nbre = x/log(x)
    else:
        nbre = (x/log10(x))/2
    return nbre

def piNormal(x):
    if x ==1:
        return 0
    n = 0
    for i in range(2,x+1):
        if isPremier(i):
            n += 1
    return n

def erreurPi(x):
    return abs(pi(x) - piNormal(x))

x = 200

pi(x)
piNormal(x)
er = pi(x) - piNormal(x)
er
def getAllProbaList(x):
    axeX = [i for i in range(1, x+1)]
    piLog = [pi(i) for i in axeX]
    distributionLog = [nbreP/i for nbreP, i in zip(piLog, axeX)]
    integralLog = (sum(distributionLog)/len(distributionLog)) * len(axeX)
    proba = [distri/integralLog for distri in distributionLog]
    return proba

def getPrimeProbaList(x):
    axeX = [i for i in primeList(x)]
    piLog = [pi(i) for i in axeX]
    distributionLog = [nbreP/i for nbreP, i in zip(piLog, axeX)]
    integralLog = (sum(distributionLog)/len(distributionLog)) * len(axeX)
    proba = [distri/integralLog for distri in distributionLog]
    return proba
    
x = 25
y = getPrimeProbaList(x)
z = sum(y)

# plt.figure(1)
# axeX = [i for i in range(1, x)]
# normal = [piNormal(i) for i in axeX]
# piLog = [pi(i) for i in axeX]
# erreurY = [erreurPi(j) for j in axeX]

# distributionLog = [nbreP/i for nbreP, i in zip(piLog, axeX)]
# distributionBrute = [nbreP/i for nbreP, i in zip(normal, axeX)]

# integralLog = (sum(distributionLog)/len(distributionLog)) * len(axeX)
# proba = [distri/integralLog for distri in distributionLog]

# plt.xlabel("Numbers")
# plt.ylabel("Number of prime numbers")

# lignes = plt.plot(axeX, erreurY, 'b', axeX, normal, 'y', axeX, piLog, 'r')
# plt.legend(lignes, ['Error', 'Dénombrement', 'Raprochement via (2x/log10(x))']);

# plt.figure(2)
# plt.plot(axeX, distributionLog, axeX, distributionBrute)



# plt.figure(3)
# plt.plot(axeX, getProbaList(x))
# plt.show()
# print("Somme:", sum(proba))




piNormal(2)
pi(2)
2/log(2)