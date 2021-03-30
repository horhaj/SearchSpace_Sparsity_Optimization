from prime import isPremier, primeList, getPrimeProbaList, getAllProbaList
from action_functions import sparsity
from random import choices
import matplotlib.pyplot as plt

x = 20
MAXLOOPTIME = 6

CATEGORY = ['K', 'C', 'OY', 'OX', 'FY', 'FX']

def generateTemporalMapping(x, MAXLOOPTIME, CATEGORY):
    xList = primeList(x)
    xProba = getPrimeProbaList(x)
    loopProba = getAllProbaList(MAXLOOPTIME + 1)[1:]
    temporalMapping = []

    for cat in CATEGORY:
        loopTime = choices(list(range(MAXLOOPTIME)), loopProba)
        s = choices(xList, weights= xProba)[0]
        #print("loopTime: ",loopTime, "s: " , s)
        temporalMapping += [(cat, s)]
        for i in range(loopTime[0]):
         #   print("gottin")
            s = choices(xList, weights= xProba)[0]
            temporalMapping += [(cat, s)]
    return temporalMapping

sparsityList = []
PRECISION = 50
xAxe = list(range(6,100))
for i in xAxe:
    if i%10 == 0:
        print(i)
    sparsityCumul = 0
    for j in range(PRECISION):
        mapping = generateTemporalMapping(i, MAXLOOPTIME, CATEGORY)
        sparsityCumul += sparsity(mapping)
    meanSparsity = sparsityCumul/PRECISION
    sparsityList += [meanSparsity]


plt.plot(xAxe, sparsityList)
plt.xlabel("Size of Temporal Mapping")
plt.ylabel("Sparsity")
plt.show()


