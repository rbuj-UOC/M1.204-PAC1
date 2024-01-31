from numpy import *
from iaa import data as UOC_D
from iaa import pca as UOC_PCA

print "Activitat: 1"

# llegir dades fitxers
prova = UOC_D.llegiex_valors("iogurts_prova.data")
print prova

print UOC_PCA.PCA_dict(prova)
