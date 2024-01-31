from math import sqrt

# Coeficient de Pearson entre dos diccionaris
def coef_pearson(dic1, dic2):
    # Obtenir els elements comuns als dos diccionaris
    comuns = [x for x in dic1 if x in dic2]
    nComuns = float(len(comuns))    
    # Si no hi ha comuns, es retorna zero; si no es calcula el coeficient
    if nComuns==0:
        return 0
    # Calcul de les mides de cada diccionari
    mitjana1 = sum([dic1[x] for x in comuns])/nComuns
    mitjana2 = sum([dic2[x] for x in comuns])/nComuns
    # Calcul del numeror i del denominador
    num = sum([(dic1[x]-mitjana1)*(dic2[x]-mitjana2) for x in comuns])
    den1 = sqrt(sum([pow(dic1[x]-mitjana1, 2) for x in comuns]))
    den2 = sqrt(sum([pow(dic2[x]-mitjana2, 2) for x in comuns]))
    den = den1*den2
    # Calcul del coeficient si es possible, o retorna zero
    if den==0:
        return 0
    return ((num/den)+1)/2
