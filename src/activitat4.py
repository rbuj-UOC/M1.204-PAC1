#! /usr/bin/python
from math import *
from functools import reduce
from random import randrange
from itertools import repeat
from numpy import *
from numpy import linalg as LG
from types import *
from iaa import data as UOC_D
from iaa import euclidean as UOC_E

def afegir_vector(vector, valor):
    aux = zeros([len(vector)+1], int)
    if len(vector)>1:
        aux[0:len(vector)]=vector[0:len(vector)]
    aux[len(vector)]=valor
    return aux

def cerca_index(vector, valor):
    res = []
    for i in range(len(vector)):
        if vector[i]==valor:
            res = afegir_vector(res, i)
    return res

def kmeans(k, maxit, train, numelem):
    # taula amb la informacio d'entrenament per als centrodes
    conj = list(map(lambda x: [float(v) for c,v in entrenament[x[1]].items() if c<=numelem], enumerate(entrenament)))
    # generar 4 centres inicials de forma aleatoria amb les dades del vector d'entrenament
    centr = [conj[randrange(len(conj))] for i in range(k)]
    for i in range(k):
        for j in range(k):
            if j != i:
                while centr[i] == centr[j]:
                    centr[i] = conj[randrange(len(conj))]
    # Repetir la cerca k centres tenint en compte la proximitat als centres
    anteriors = None
    # per a cada punt d'entrenamanet determinar a quin grup esta mes aprop
    distancies  = list( map( lambda x: map(lambda y: UOC_E.dist_euclidiana_iguals(conj[x],centr[y]), range(len(centr))), range(len(conj)) ) )
    # pertinensa, llista amb les pertinenses dels elements d'entrenament als grups
    pertinensa = list( map(lambda x: distancies[x].index(min(distancies[x])), range(len(distancies)) ))
    for it in range(maxit):
        # Recalcular els nous centroides dels k grups, que estaran en el centre geometric del conjunt de punts del grup.
        for i in range(k):
            # conj_grup conjunt amb els indexs dels elements d'entrenament que formen part d'un grup
            conj_grup = filter(lambda x: pertinensa[x] == i, range(len(pertinensa)))
            if type(conj_grup) is BooleanType:
                centr[i] = conj[randrange(len(conj))]
                print "fix 1: volta",it
            else:
                if len(conj_grup)==0:
                    centr[i] = conj[randrange(len(conj))]
                    print "fix 2: volta",it
                else:
                    # calcular la mitja aritmetica de cada variable
                    cetre_geometric = zeros([numelem], float)
                    for j in range(len(conj_grup)):
                        for p in range(numelem):
                            cetre_geometric[p] = cetre_geometric[p] + conj[conj_grup[j]][p]
                    cetre_geometric = cetre_geometric * (1.0 / float(len(conj_grup)))
                    # el centre de cada grup es el nou centre geometric
                    centr[i] = cetre_geometric
        # per a cada punt d'entrenamanet determinar a quin grup esta mes aprop
        distancies  = list( map( lambda x: map(lambda y: UOC_E.dist_euclidiana_iguals(conj[x],centr[y]), range(len(centr))), range(len(conj)) ) )
        # pertinensa, llista amb les pertinenses dels elements d'entrenament als grups
        pertinensa = list( map(lambda x: distancies[x].index(min(distancies[x])), range(len(distancies)) ))
        # Aturar en cas que no hi hagin canvis en la pertinensa 
        if pertinensa == anteriors: break
        anteriors = pertinensa
    return centr, pertinensa


print "Activitat: 4"

# Carregar dades d'entrenament
entrenament = UOC_D.llegiex_valors("iogurts_entrenament.data")
# trobar k nodes centroides en maxit iteracions
k = 4
maxit = 10
centroides, pertinensa = kmeans(k, maxit, entrenament, 6)
# trobar el iogurt preferit dels nous de cada grup [(movieId, count)]
res = zeros((k,4),int)
for g in range(len(pertinensa)): # 0..100
    for t in range(0,4):
        if entrenament[g+1][t+7]==5:
            res[pertinensa[g]][t] += 1
iogurt_grup  = map(lambda x: cerca_index(res[x], max(res[x]))+7, range(k))
print "Encert iogurt mes recomanat:",(float( sum(map(lambda x: max(res[x]), range(k))) ) / float(len(pertinensa)) ) * 100.0, "% (grup entrenament)"
for i in range(k):
    print "Iogurt(s) pregerit(s) grup",i,"=",iogurt_grup[i]
# Carregar dades de prova
prova      = UOC_D.llegiex_valors("iogurts_prova.data")
# distancies entre element de la prova i el centroide
distancies = list( map( lambda x: map(lambda y: UOC_E.dist_euclidiana_iguals([v for c,v in prova[x].items()],centroides[y]), range(k) ), prova.keys() ))
# l'element de la prova pertany al grup amb distancia menor al centoide de cada grup
pertinensa = list( map(lambda x: distancies[x].index(min(distancies[x])), range(len(distancies)) ))
# recomanacio segons la pertinensa a un grup
prediccions= {x+101: list(iogurt_grup[pertinensa[x]]) for x in range(len(pertinensa))}
print "Prediccio (idPersona, iogurts) =", prediccions
# Carregar dades de prova
validacio  = UOC_D.llegiex_valors("iogurts_validacio.data")
# Encert prediccio iogurt mes valorat:
encert=0
for i in validacio.keys():
    if validacio[i][prediccions[i][0]]==5:
        encert +=1
print "Percentatge d'encerts en prediccio iogurt mes valorat:",(float(encert) / float(len(validacio))) * 100.0, '%'
# Encert prediccio iogurts mes valorats:
encert=0
for i in validacio.keys():
    if validacio[i][prediccions[i][0]]>=4:
        encert +=1
print "Percentatge d'encerts en prediccions dins dels 2 mes valorats:",(float(encert) / float(len(validacio))) * 100.0, '%'