from itertools import permutations
import time

L = [i for i in range(100)] 
W = [('K', 12), ('C', 4), ('C', 4), ('OX', 13), ('FX', 3), ('K', 4), ('C', 8), ('K', 4)] 
I = [[('K', 12), ('C', 4)], [('C', 4), ('OX', 13), ('FX', 3), ('K', 4)], [('C', 8), ('K', 4)]]  
O = [[('K', 12), ('C', 4), ('C', 4)], [('OX', 13), ('FX', 3), ('K', 4), ('C', 8)], [('K', 4)]]  

mapping = [(6, 2), (4, 13), (5, 2), (2, 3), (5, 2), (3, 13), (6, 2), (6, 3), (1, 3), (5, 2), (5, 2), (6, 2), (5, 2), (5, 2), (6, 2), (7, 1), (6, 2), (5, 2), (6, 2), (5, 2), (6, 2)]
len(mapping)

cat = list(zip(*W))

print(W[0][0][0])

def deE(w):
    n = 0
    for i in w:
        n += len(i)
    return n

print(deE(W), deE(I), deE(O))

def getTranspoDistincteIndiceByLen(n):
    ensembleTn = []
    for i in range(n):
        for j in range(i+1, n):
            ensembleTn += [(i, j)]
    return ensembleTn

def getTranspoDistincteIndice(ensemble):
    ensembleTn = []
    n = len(ensemble)
    for i in range(n):
        for j in range(i+1, n):
            ensembleTn += [(i, j)]
    return ensembleTn

def getTranspoDistincte(ensemble):
    ensembleTn = []
    for i in range(len(ensemble)):
        for j in range(i+1, len(ensemble)):
            ensembleTn += [(ensemble[i], ensemble[j])]
    return ensembleTn

# index 0 a fixe a laplace d'index 1 pour math
# 
#
def getTranspo(categorie, w):
    index = []
    for i in range(len(w)):
        if categorie == w[i]:
            index += [i]
    print(index)
    return getTranspoDistincte(index)

def getBadTranspo(w):
    tabu = []
    badTranspo = []
    categories = list(zip(*w))[0]
    transpo = (0, 0)
    for i in range(len(categories)):
        if categories.count(categories[i]) > 1 and categories[i] not in tabu:
            tabu += [categories[i]]
            badTranspo += [getTranspo(categories[i], categories)]
    return badTranspo

def transCleaning(transpositions, badTranspositions):
    for badTranspoByCat in badTranspositions:
        for badTranspo in badTranspoByCat:
                transpositions.remove(badTranspo)
    return transpositions

def getSetAction(map):
    transpositionParIndice = getTranspoDistincteIndice(mapping)
    badTranspo = getBadTranspo(mapping)
    cleanedTranspo = transCleaning(transpositionParIndice, badTranspo)
    return cleanedTranspo

l = [1,2,5,6]
s = [] + l + []
###########################-----------Testing-------------#######################################
start_time = time.time()

transpositionParIndice = getTranspoDistincteIndice(mapping)
badTranspo = getBadTranspo(mapping)
cleanedTranspo = transCleaning(transpositionParIndice, badTranspo)

print("\n---------------------------------------------------------------------------------------------------------------\n"*2)
print("Transpo par Indice: ", transpositionParIndice)
print("\n---------------------------------------------------------------------------------------------------------------\n"*2)
print("badTranspo: ", badTranspo)
print("\n---------------------------------------------------------------------------------------------------------------\n"*2)
print("Cleaned Transpo: ", cleanedTranspo)

print("--- %s seconds ---" % (time.time() - start_time))
#
