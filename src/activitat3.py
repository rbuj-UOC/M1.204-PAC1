
from numpy import *
from iaa import data as UOC_D
from iaa import euclidean as UOC_E
from iaa import clustering as UOC_C
from heapq import merge

print "Activitat: 3"
print

# llegir fitxer de prova
prova = UOC_D.llegiex_valors("iogurts_prova.data")

# llegir fitxer de validacio
validacio = UOC_D.llegiex_valors("iogurts_validacio.data")

# Enllac simple
print "Enllac simple:"
# generacio del grup
grup = UOC_C.agrupamentAglomeratiu(prova, 4, UOC_C.enllacSimple, dist=UOC_E.dist_euclidiana_diferents)
# Predicio
iogurt_grup = {g: [elem for elem in validacio[g] if validacio[g][elem]==5][0] for g in grup}
prediccions = list(merge( map( lambda x: map( lambda y: {grup[x][y]: iogurt_grup[x]}, range(len(grup[x])) ), grup ) ))
t ={}
for v in prediccions:
    for d in v:
        t = dict(t.items() + d.items())
prediccions = t
print "Prediccio (idPersona: iogurts) =",prediccions
# Encert
encert=0
for i in validacio.keys():
    if validacio[i][prediccions[i]]==5:
        encert +=1
print "Percentatge d'encerts en prediccio iogurt mes valorat:",(float(encert) / float(len(validacio))) * 100.0, '%'
# Encert prediccio iogurts mes valorats:
encert=0
for i in validacio.keys():
    if validacio[i][prediccions[i]]>=4:
        encert +=1
print "Percentatge d'encerts en prediccions dins dels 2 mes valorats:",(float(encert) / float(len(validacio))) * 100.0, '%'


print
print "Enllac complex:"
grup = UOC_C.agrupamentAglomeratiu(prova, 4, UOC_C.enllacComplet, dist=UOC_E.dist_euclidiana_diferents)
# Predicio
iogurt_grup = {g: [elem for elem in validacio[g] if validacio[g][elem]==5][0] for g in grup}
prediccions = list(merge( map( lambda x: map( lambda y: {grup[x][y]: iogurt_grup[x]}, range(len(grup[x])) ), grup ) ))
t ={}
for v in prediccions:
    for d in v:
        t = dict(t.items() + d.items())
prediccions = t
print "Prediccio (idPersona: iogurts) =",prediccions
# Encert
encert=0
for i in validacio.keys():
    if validacio[i][prediccions[i]]==5:
        encert +=1
print "Percentatge d'encerts en prediccio iogurt mes valorat:",(float(encert) / float(len(validacio))) * 100.0, '%'
# Encert prediccio iogurts mes valorats:
encert=0
for i in validacio.keys():
    if validacio[i][prediccions[i]]>=4:
        encert +=1
print "Percentatge d'encerts en prediccions dins dels 2 mes valorats:",(float(encert) / float(len(validacio))) * 100.0, '%'


print
print "Enllac mitjana:"
grup = UOC_C.agrupamentAglomeratiu(prova, 4, UOC_C.enllacMitja, dist=UOC_E.dist_euclidiana_diferents)
# Predicio
iogurt_grup = {g: [elem for elem in validacio[g] if validacio[g][elem]==5][0] for g in grup}
prediccions = list(merge( map( lambda x: map( lambda y: {grup[x][y]: iogurt_grup[x]}, range(len(grup[x])) ), grup ) ))
t ={}
for v in prediccions:
    for d in v:
        t = dict(t.items() + d.items())
prediccions = t
print "Prediccio (idPersona: iogurts) =",prediccions
# Encert
encert=0
for i in validacio.keys():
    if validacio[i][prediccions[i]]==5:
        encert +=1
print "Percentatge d'encerts en prediccio iogurt mes valorat:",(float(encert) / float(len(validacio))) * 100.0, '%'
# Encert prediccio iogurts mes valorats:
encert=0
for i in validacio.keys():
    if validacio[i][prediccions[i]]>=4:
        encert +=1
print "Percentatge d'encerts en prediccions dins dels 2 mes valorats:",(float(encert) / float(len(validacio))) * 100.0, '%'
