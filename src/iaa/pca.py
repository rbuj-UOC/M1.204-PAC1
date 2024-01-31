from numpy import *

def PCA_dict(prova):
    l = zeros((len(prova)*6,3),int) # cada element te sis valors
    d = zeros((len(prova),6),int)
    i=0
    j=0
    for x in prova:
        k=0
        for y in prova[x]:
            l[i][0]=x
            l[i][1]=y
            l[i][2]=prova[x][y]
            d[j][k]=prova[x][y]
            i=i+1
            k=k+1
        j=j+1
    # Pas 1 PCA: trobar la matriu de covarianca
    # d.mean(0) valor mig dels elements de cada culuma, dimensio mxn:
    # retorna n valors [sum(:,0)/n, sum(:,1)/n, ..., sum(:,n-1)/n]
    # valor anomenat com: mitja aritmetica
    d1 = d - d.mean(0) # d1 es la dispersio al voltant de la mitjana
    # Matriu de covarianca = At x A
    matcov = dot(d1.T,d1)
    # Pas 2 PCA: trobar valors i vectors propis
    valp1,vecp1 = linalg.eig(matcov)
    # ordenacio
    ind_creixent = argsort(valp1) # ordre creixent
    ind_decre = ind_creixent[:: -1] # ordre decreixent
    val_decre = valp1[ind_decre] # valors propis en ordre decreixent
    vec_decre = vecp1[:,ind_decre] # ordenar tambe vectors propis
    # Projectar dades a la nova base definida pels dos
    # vectors propis amb mes valor propi ( espai PCA 2D)
    orig_means = d.mean(0)
    d_PCA2 = zeros((d.shape[0],5))
    for i in range(d.shape[0]):
        for j in range(2):
            d_PCA2[i,j] = dot(d1[i,:],vec_decre[:,j])
    # Recuperar
    d_recon2 = zeros((d.shape[0],d.shape[1]))
    for i in range(d.shape[0]):
        d_recon2[i] = orig_means
        for j in range(2):
            d_recon2[i] += d_PCA2[i,j]*vec_decre[:,j]
    # formatar PCA recuperada amb diccionaris
    d = zeros((len(prova)*6,3))
    i=0
    j=0
    for x in prova:
        k=0
        for y in prova[x]:
            d[i][0]=l[i][0]
            d[i][1]=l[i][1]
            d[i][2]=d_recon2[j][k]
            k=k+1
            i=i+1
        j=j+1
    prova_pca = {int(l[0]) : {}  for l in d}
    for l in d:
        prova_pca[int(l[0])][int(l[1])] = l[2]
    return prova_pca