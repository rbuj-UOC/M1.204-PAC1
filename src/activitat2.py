from numpy import *
from numpy import linalg as LG
from iaa import data as UOC_D
from iaa import euclidean as UOC_E
from iaa import pearson as UOC_P
from iaa import ratings as UOC_R
from iaa import pca as UOC_PCA


print "Activitat: 2"
print

# llegir dades fitxers
entrenament = UOC_D.llegiex_valors("iogurts_entrenament.data")
prova = UOC_D.llegiex_valors("iogurts_prova.data")
validacio = UOC_D.llegiex_valors("iogurts_validacio.data")

# Recomanador ponderat amb similitud euleriana
print "Similitud Euleriana:"
recomanacio = {x: UOC_R.weightedRating(prova, entrenament, x, UOC_E.simul_euclidiana_diferents) for x in prova}
# llista de prediccions iogurt mes ben valorat
prediccions = {perso: [elem for elem in recomanacio[perso] if recomanacio[perso][elem]==5][0] for perso in recomanacio}
print "Prediccio similitud (idPersona, iogurts) =", prediccions
# Encert prediccio iogurt mes valorat:
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

# Recomanador ponderat amb coeficient pearson
print "Similitud coef. Perason:"
recomanacio = {x: UOC_R.weightedRating(prova, entrenament, x, UOC_P.coef_pearson) for x in prova}
# llista de prediccions iogurt mes ben valorat
prediccions = {perso: [elem for elem in recomanacio[perso] if recomanacio[perso][elem]==5][0] for perso in recomanacio}
print "Prediccio similitud pearson (idPersona, iogurts) =", prediccions
# Encert prediccio iogurt mes valorat:
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
print "PCA"
print
prova = UOC_PCA.PCA_dict(prova)


# Recomanador ponderat amb similitud euleriana
print "Similitud Euleriana:"
recomanacio = {x: UOC_R.weightedRating(prova, entrenament, x, UOC_E.simul_euclidiana_diferents)
    for x in prova}
# llista de prediccions iogurt mes ben valorat
prediccions = {perso: [elem for elem in recomanacio[perso] if recomanacio[perso][elem]==5][0] for perso in recomanacio}
print "Prediccio similitud (idPersona, iogurts) =", prediccions
# Encert prediccio iogurt mes valorat:
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

# Recomanador ponderat amb coeficient pearson
print "Similitud coef. Perason:"
recomanacio = {x: UOC_R.weightedRating(prova, entrenament, x, UOC_P.coef_pearson) for x in prova}
# llista de prediccions iogurt mes ben valorat
prediccions = {perso: [elem for elem in recomanacio[perso] if recomanacio[perso][elem]==5][0] for perso in recomanacio}
print "Prediccio similitud pearson (idPersona, iogurts) =", prediccions
# Encert prediccio iogurt mes valorat:
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
