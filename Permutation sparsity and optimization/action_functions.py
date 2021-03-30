from itertools import permutations
import time

L = [i for i in range(100)] 
W = [('K', 12), ('C', 4), ('C', 4), ('OX', 13), ('FX', 3), ('K', 4), ('C', 8), ('K', 4)] 
I = [[('K', 12), ('C', 4)], [('C', 4), ('OX', 13), ('FX', 3), ('K', 4)], [('C', 8), ('K', 4)]]  
O = [[('K', 12), ('C', 4), ('C', 4)], [('OX', 13), ('FX', 3), ('K', 4), ('C', 8)], [('K', 4)]]  

mapping = [(6, 2), (4, 13), (5, 2), (2, 3), (5, 2), (3, 13), (6, 2), (6, 3), (1, 3), (5, 2), (5, 2),
            (6, 2), (5, 2), (5, 2), (6, 2), (7, 1), (6, 2), (5, 2), (6, 2), (5, 2), (6, 2)]
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

def getBadSucc(j, categories):
    if j == len(categories):
        return [] 
    elif categories[j+1] == categories[j]:
        return [(j, j+1)]
    else :return []
        
def getBadTranspo(w):
    tabu = []
    badTranspo = []
    zippedW = list(zip(*w))
    categories, blocks = zippedW[0], zippedW[1]
    for i in range(len(categories) - 1):
        cat = categories[i]
        if categories[i:].count(cat) > 1:
            tabu += [cat]
            badTranspo += getBadSucc(i, categories)
            for j in range(i+2, len(categories)):
                if categories[j] == cat and blocks[i] == blocks[j]:
                    badTranspo += [(i, j)]
                    # Matnsach hadchi rah mohim optimisation
                    # Rajoute une fonction qui check si le suivant est de la meme cat
                    # tu auras donc for cat in cats where cat == ncat: rajoute successeur si existe 
                    # Puis check all same blocks
            #badTranspo += [getTranspo(cat, categories, blocks)]
    return badTranspo

def transCleaning(transpositions, badTranspositions):
    cleanedTranspo = transpositions[:]
    for badTranspo in badTranspositions:
        cleanedTranspo.remove(badTranspo)
    return cleanedTranspo

def getSetAction(map):
    transpositionParIndice = getTranspoDistincteIndice(mapping)
    badTranspo = getBadTranspo(mapping)
    cleanedTranspo = transCleaning(transpositionParIndice, badTranspo)
    return cleanedTranspo

def sparsity(mapping):
    transpositionParIndice = getTranspoDistincteIndice(mapping)
    badTranspo = getBadTranspo(mapping)
    return len(badTranspo)/len(transpositionParIndice)

[0, 6, 11, 14, 16, 18, 20]
l = [1,2,5,6]
s = [] + l + []

###########################-----------Testing-------------#######################################
start_time = time.time()

transpositionParIndice = getTranspoDistincteIndice(mapping)
badTranspo = getBadTranspo(mapping)
cleanedTranspo = transCleaning(transpositionParIndice, badTranspo)

print("\n---------------------------------------------------------------------------------------------------------------\n"*2)
print("Transpo par Indice: ", transpositionParIndice)
print("\nlen : ", len(transpositionParIndice))
print("\n---------------------------------------------------------------------------------------------------------------\n"*2)
print("badTranspo: ", badTranspo)
print("\nlen : ", len(badTranspo))
print("\n---------------------------------------------------------------------------------------------------------------\n"*2)
print("Cleaned Transpo: ", cleanedTranspo)
print("\nlen : ", len(cleanedTranspo))

print("\n--- %s seconds ---" % (time.time() - start_time))
#
