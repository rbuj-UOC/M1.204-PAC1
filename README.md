# PAC1: recomanadors i agrupaments Enunciat

## Introducció

L'empresa productora de iogurts Yuggoth S.A. ha fet un estudi entre els seus consumidors habituals per tal de conèixer la valoració que fan de cadascun dels seus sis sabors de iogurt i també per conèixer les valoracions dels consumidors pel que fa a quatre nous sabors que volen comercialitzar en un futur.

## Dades

Tots els arxius de dades (iogurts_*.data) tenen el mateix format: tres columnes amb l'identificador d'usuari, l'identificador del iogurt i la valoració (1..5) respectivament. Els iogurts amb identificador 1..6 són els iogurts que actualment fabrica Yuggoth, mentre que els iogurts amb identificador 7..10 són els nous sabors que vol comercialitzar.

Al fitxer iogurts_entrenament.data hi ha les valoracions de 100 consumidors (amb identificadors 1..100) de tots deu iogurts, amb la particularitat què amb els nous sabors no poden repetir valoració (de fet han de repartir les valoracions 2..5 entre els quatre iogurts nous). El fitxer iogurts_prova.data conté les valoracions d'altres 100 consumidors (amb identificadors 101..200) però només del iogurts que es venen actualment (1..6). Finalment, el fitxer iogurts_validacio.data conté les valoracions que els 100 consumidors del fitxer iogurts_prova (és a dir, els que tenen els identificadors 101..200) han fet dels nous iogurts (7..10), també amb la restricció de no repetir valoracions.

Nota: el fet que les valoracions dels nous iogurts no es puguin repetir per un mateix consumidor serveix per evitar ambigüitats als resultats i simplificar l'anàlisi i la valoració dels resultats. De fet és força habitual imposar aquesta mena de restriccions als estudis de mercat.


## Activitats

Per resoldre aquesta PAC heu de fer servir el codi dels programes 2.2-2.7 amb les modificacions escaients per treballar amb els nous fitxers de dades. També fareu servir el codi 4.4 (k-means).

A totes les activitats cal justificar raonadament la vostra resposta.

### Activitat 1

El pas previ a qualsevol anàlisi de dades és efectuar un tractament per tal d'adequar els seus valors. Entre les operacions habituals trobem la normalització o estandardització de les dades (veieu per exemple http://ca.wikipedia.org/wiki/Distribuci%C3%B3_normal).

Primer de tot es demana, doncs, que realitzeu el tractament previ de les dades que considereu necessari (o pot ser no cal fer-ne cap tractament previ).

**Resposta**

Ja que en la realització de les següents activitats es fan operacions element sobre element, per exemple en el càlcul de distàncies i/o similituds eulerianes i/o coeficients de Pearson, i com que la informació està indexada segons un identificador d'usuari, es creu convenient utilitzar la representació de dades en format diccionari i no en matrius, per la qual cosa no es realitza a priori una representació de la informació en format de matriu així com tampoc es realitza cap adaptació per facilitar les operacions matemàtiques amb l'ús de matrius, ja que s'utilitzen diccionaris.

Les dades no requereixen cap normalització ja que les dades de prova i les dades d'entrenament tenen el mateix recorregut (diferència entre el valor major i valor menor d'una variable estadística r = 5-1 = 4). De no ser així s'haurien hagut de normalitzar les dades (centrant el valor a zero al restar-los-hi la variança. Posteriorment escollir una escala i multiplicar els valor pel factor d'anivellament [-v/2, v/2]. Per últim centrar les dades sumant-hi v/2).

En el segon exercici es va provar de millorar la informació eliminant aquella menys significativa utilitzant PCA, no obstant no es va veure cap millora quantitativa en els resultats.

### Activitat 2

Prenent les dades del fitxer d'entrenament, genereu un recomanador ponderat de iogurts nous pels consumidors de prova (identificadors 101..200), de manera que a cadascun d'aquests consumidors se li recomani quin dels nous iogurts l'hauria d'agradar més tenint en compte les valoracions dels consumidors d'entrenament (1..100). Proveu amb similitud euclidiana i amb correlació de Pearson com a mides de similitud.

Seguidament, compareu la recomanació feta per cada usuari (serà un dels iogurts 7..10) amb les seves valoracions enregistrades al fitxer de validació. En quin tant per cent dels casos la recomanació coincideix amb una valoració de 5? I de 4? Quines conclusions es poden treure?

Compareu les diferències (si hi ha) entre les recomanacions amb similitud euclidiana i amb correlació de Pearson.

**Resposta**

El percentatge d'encert quant al iogurt amb millor valoració, és més elevat si s'utilitza similitud per coeficients de Pearson en comparació amb l'ús de similitud euleriana. No obstant el percentatge d'encert com a iogurts més ben valorats, ambdues similituds ofereixen valors semblants. (Percentatge encert millor valorat similitud euleriana: 51%, coeficient Pearson:58%. Percentatge encert entre més ben valorats similitud euleriana: 70%, coeficient Pearson:74%)

```
Similitud Euleriana:
Predicció similitud (idPersona, iogurts) = {101: 7, 102: 8, 103: 9, 104: 8, 105: 9, 106: 8, 107: 8, 108: 7, 109: 8, 110: 7, 111: 7, 112: 8, 113: 8, 114: 7, 115: 7, 116: 8, 117: 8, 118: 7, 119: 7, 120: 8, 121: 8, 122: 7, 123: 8, 124: 8, 125: 8, 126: 8, 127: 8, 128: 7, 129: 8, 130: 7, 131: 8, 132: 8, 133: 8, 134: 8, 135: 8, 136: 8, 137: 8, 138: 8, 139: 9, 140: 8, 141: 8, 142: 7, 143: 8, 144: 9, 145: 8, 146: 7, 147: 8, 148: 8, 149: 7, 150: 8, 151: 8, 152: 7, 153: 8, 154: 8, 155: 8, 156: 7, 157: 8, 158: 8, 159: 7, 160: 8, 161: 8, 162: 7, 163: 7, 164: 8, 165: 9, 166: 8, 167: 8, 168: 8, 169: 8, 170: 7, 171: 9, 172: 8, 173: 8, 174: 8, 175: 8, 176: 8, 177: 9, 178: 8, 179: 7, 180: 8, 181: 8, 182: 8, 183: 8, 184: 8, 185: 8, 186: 8, 187: 8, 188: 9, 189: 8, 190: 8, 191: 8, 192: 9, 193: 7, 194: 8, 195: 8, 196: 8, 197: 8, 198: 8, 199: 7, 200: 9}
Percentatge d'encerts en predicció iogurt mes valorat: 51.0 %
Percentatge d'encerts en prediccions dins dels 2 mes valorats: 70.0 %

Similitud coef. Perason:
Predicció similitud pearson (idPersona, iogurts) = {101: 9, 102: 10, 103: 9, 104: 8, 105: 9, 106: 8, 107: 8, 108: 7, 109: 9, 110: 7, 111: 7, 112: 8, 113: 9, 114: 7, 115: 10, 116: 9, 117: 8, 118: 7, 119: 7, 120: 7, 121: 7, 122: 7, 123: 8, 124: 8, 125: 8, 126: 8, 127: 8, 128: 7, 129: 8, 130: 7, 131: 8, 132: 8, 133: 9, 134: 8, 135: 8, 136: 8, 137: 8, 138: 8, 139: 9, 140: 8, 141: 8, 142: 7, 143: 8, 144: 9, 145: 9, 146: 7, 147: 8, 148: 8, 149: 7, 150: 8, 151: 9, 152: 7, 153: 7, 154: 10, 155: 9, 156: 7, 157: 8, 158: 8, 159: 7, 160: 8, 161: 7, 162: 7, 163: 7, 164: 8, 165: 9, 166: 8, 167: 8, 168: 8, 169: 8, 170: 7, 171: 9, 172: 8, 173: 8, 174: 8, 175: 8, 176: 8, 177: 9, 178: 8, 179: 7, 180: 7, 181: 7, 182: 8, 183: 7, 184: 8, 185: 8, 186: 8, 187: 8, 188: 9, 189: 8, 190: 8, 191: 8, 192: 9, 193: 7, 194: 8, 195: 9, 196: 8, 197: 8, 198: 7, 199: 8, 200: 9}
Percentatge d'encerts en predicció iogurt mes valorat: 58.0 %
Percentatge d'encerts en prediccions dins dels 2 mes valorats: 74.0 %
```

En aquesta activitat, els resultats obtinguts amb similitud euleriana són deguts al fet que en el càlcul de la similitud entre usuaris sempre es té el mateix nombre de valoracions en el seu càlcul per a la predicció, i les valoracions de tots els usuaris comparteixen la mateixa escala. Per aquest motiu amb els coeficients de Pearson s'assoleix un percentatge d'encert més elevat per al més ben valorat, i amb similitud euleriana lleugerament superior quant a l'encert dins dels més ben valorats. Si es normalitzen els valors, en aquest cas amb PCA, disminueix l'encert global en les prediccions però s'igualen els resultats en l'estimació en totes les valoracions.

### Activitat 3

Genereu un dendrograma pel mètode aglomeratiu que faci l'agrupament dels consumidors fent servir només les dades del fitxer de prova. No cal generar el diagrama d'arbre, només ens interessen els grups generats.

Hauríeu d'obtenir una sèrie d'agrupaments de consumidors; preneu com a resultat l'agrupament en el qual queden exactament quatre grups. Ara accediu al fitxer de validació i determineu quin és el iogurt més valorat per cada usuari. Associeu aquesta informació amb els grups obtinguts amb el dendrograma: els grups són uniformes a les seves valoracions dels nous iogurts? És a dir, quin tant per cent de cada grup prefereix el mateix iogurt (dels nous)?

Podeu comparar els resultats fent servir els diferents mètodes d'enllaç que hi ha als materials de l'assignatura.

**Resposta**

L'enllaç simple va obtenir el percentatge d'encert més baix en la predicció del iogurt més ben valorat, molt inferior al percentatge d'encert utilitzant enllaç complet o amb mitjana, amb els darrers enllaços es van obtenir resultats amb rang lleugerament similars, però superior en el cas d'enllaç  amb mitjana. (Percentatge encert enllaç simple: 26%, enllaç complet:43% i enllaç amb mitjana:53%)

Quant al percentatge d'encert dins dels més ben valorats, tots tres van obtenir percentatges d'encert dins d'un rang més similar, el més baix va ser amb enllaç simple. Per a l'enllaç complet el percentatge va ser pràcticament idèntic a l'aconseguit per l'enllaç amb mitjana. (Percentatge encert enllaç simple: 52%, enllaç complet:69% i enllaç amb mitjana:68%)

```
Enllaç simple
Predicció (idPersona: iogurts) = {101: 9, 102: 9, 103: 9, 104: 9, 105: 9, 106: 9, 107: 9, 108: 9, 109: 9, 110: 9, 111: 9, 112: 9, 113: 9, 114: 9, 115: 9, 116: 9, 117: 9, 118: 9, 119: 9, 120: 9, 121: 9, 122: 9, 123: 9, 124: 9, 125: 9, 126: 9, 127: 9, 128: 9, 129: 9, 130: 9, 131: 9, 132: 9, 133: 9, 134: 9, 135: 9, 136: 9, 137: 9, 138: 9, 139: 9, 140: 9, 141: 9, 142: 9, 143: 9, 144: 9, 145: 9, 146: 9, 147: 9, 148: 9, 149: 9, 150: 9, 151: 9, 152: 9, 153: 9, 154: 9, 155: 9, 156: 9, 157: 9, 158: 9, 159: 10, 160: 9, 161: 9, 162: 9, 163: 9, 164: 9, 165: 9, 166: 9, 167: 9, 168: 9, 169: 9, 170: 9, 171: 9, 172: 9, 173: 9, 174: 9, 175: 9, 176: 9, 177: 9, 178: 9, 179: 9, 180: 9, 181: 9, 182: 9, 183: 9, 184: 9, 185: 9, 186: 9, 187: 9, 188: 9, 189: 9, 190: 9, 191: 9, 192: 10, 193: 9, 194: 9, 195: 9, 196: 9, 197: 9, 198: 9, 199: 9, 200: 9}
Percentatge d'encerts en predicció iogurt mes valorat: 26.0 %
Percentatge d'encerts en prediccions dins dels 2 mes valorats: 52.0 %

Enllaç complex
Predicció (idPersona: iogurts) = {101: 9, 102: 10, 103: 10, 104: 10, 105: 10, 106: 10, 107: 10, 108: 9, 109: 9, 110: 9, 111: 9, 112: 10, 113: 10, 114: 9, 115: 10, 116: 10, 117: 8, 118: 9, 119: 9, 120: 10, 121: 9, 122: 9, 123: 10, 124: 9, 125: 10, 126: 8, 127: 10, 128: 9, 129: 8, 130: 9, 131: 8, 132: 10, 133: 10, 134: 10, 135: 9, 136: 10, 137: 10, 138: 10, 139: 10, 140: 8, 141: 10, 142: 9, 143: 9, 144: 9, 145: 10, 146: 9, 147: 10, 148: 10, 149: 9, 150: 10, 151: 10, 152: 9, 153: 10, 154: 10, 155: 10, 156: 9, 157: 10, 158: 10, 159: 10, 160: 9, 161: 9, 162: 9, 163: 9, 164: 10, 165: 10, 166: 8, 167: 8, 168: 10, 169: 9, 170: 9, 171: 10, 172: 10, 173: 10, 174: 10, 175: 10, 176: 8, 177: 10, 178: 8, 179: 9, 180: 9, 181: 9, 182: 10, 183: 9, 184: 10, 185: 9, 186: 10, 187: 10, 188: 10, 189: 8, 190: 10, 191: 10, 192: 10, 193: 9, 194: 10, 195: 10, 196: 8, 197: 8, 198: 10, 199: 10, 200: 9}
Percentatge d'encerts en predicció iogurt mes valorat: 43.0 %
Percentatge d'encerts en prediccions dins dels 2 mes valorats: 69.0 %

Enllaç mitjana
Predicció (idPersona: iogurts) = {101: 9, 102: 9, 103: 9, 104: 10, 105: 9, 106: 9, 107: 10, 108: 9, 109: 9, 110: 7, 111: 7, 112: 10, 113: 9, 114: 7, 115: 9, 116: 9, 117: 10, 118: 7, 119: 7, 120: 10, 121: 9, 122: 7, 123: 9, 124: 7, 125: 10, 126: 10, 127: 10, 128: 7, 129: 10, 130: 7, 131: 10, 132: 10, 133: 9, 134: 10, 135: 10, 136: 10, 137: 10, 138: 10, 139: 9, 140: 10, 141: 10, 142: 7, 143: 7, 144: 9, 145: 9, 146: 7, 147: 10, 148: 9, 149: 7, 150: 10, 151: 9, 152: 7, 153: 10, 154: 9, 155: 9, 156: 7, 157: 10, 158: 9, 159: 10, 160: 10, 161: 9, 162: 10, 163: 7, 164: 10, 165: 9, 166: 10, 167: 10, 168: 10, 169: 7, 170: 10, 171: 9, 172: 10, 173: 10, 174: 9, 175: 9, 176: 10, 177: 9, 178: 10, 179: 10, 180: 10, 181: 7, 182: 10, 183: 9, 184: 10, 185: 10, 186: 10, 187: 10, 188: 9, 189: 10, 190: 10, 191: 10, 192: 10, 193: 7, 194: 10, 195: 9, 196: 10, 197: 10, 198: 9, 199: 10, 200: 9}
Percentatge d'encerts en predicció iogurt mes valorat: 53.0 %
Percentatge d'encerts en prediccions dins dels 2 mes valorats: 68.0 %
```

### Activitat 4

Feu servir l'algorisme k-means (el teniu al codi 4.4 dels materials) per generar quatre grups de consumidors tenint en compte només les valoracions dels iogurts 1..6 dels consumidors del fitxer d'entrenament.

Com a resultat obtindreu quatre grups de consumidors amb valoracions semblants i quatre centroides, és a dir quatre consumidors representatius de cadascun dels quatre grups.

Calculeu quin és el nou iogurt preferit (valoració igual a cinc) de cada grup. És el mateix que el preferit pel seu centroide? Per qué?

A continuació farem servir els centroides obtinguts com a recomanador basat en models per nous consumidors. Determineu a quin grup pertany cadascun dels consumidors del fitxer de prova, i com a conseqüència quin nou iogurt li recomanaríeu.

Compareu aquesta recomanació amb la seva pròpia valoració registrada al fitxer iogurts_validacio.data. Quin tant per cent d'encert s'obté (usuaris als que s'hi recomana el seu nou iogurt preferit)? I si relaxem una mica les condicions, és a dir acceptem per bona una recomanació dels iogurts amb valoració 4 o 5, quin tant per cent d'encert s'obté?

**Resposta**

El percentatge d'encert varia en cada execució, ja que al principi de l'algoritme de kmeans s'escullen k centroides a l'atzar, d'aquesta manera en cada execució canvien els centroides, els membres en cadascun dels grups, les prediccions i el percentatge d'encerts. El iogurt més preferit d'un grup és o bé el que està més a prop del centroide o aquell més preferit pels membres del grup.

```
Encert iogurt més recomanat: 68.0 % (grup entrenament)
Iogurt(s) pregerit(s) grup 0 = [8]
Iogurt(s) pregerit(s) grup 1 = [9]
Iogurt(s) pregerit(s) grup 2 = [7]
Iogurt(s) pregerit(s) grup 3 = [10]
Prediccio (idPersona, iogurts) = {101: [9], 102: [9], 103: [9], 104: [10], 105: [9], 106: [9], 107: [10], 108: [9], 109: [9], 110: [7], 111: [7], 112: [10], 113: [9], 114: [7], 115: [9], 116: [9], 117: [8], 118: [7], 119: [7], 120: [10], 121: [9], 122: [7], 123: [9], 124: [9], 125: [10], 126: [8], 127: [10], 128: [7], 129: [8], 130: [7], 131: [8], 132: [10], 133: [9], 134: [10], 135: [10], 136: [10], 137: [10], 138: [10], 139: [9], 140: [8], 141: [8], 142: [7], 143: [7], 144: [9], 145: [9], 146: [7], 147: [8], 148: [9], 149: [7], 150: [10], 151: [9], 152: [7], 153: [10], 154: [9], 155: [9], 156: [7], 157: [10], 158: [8], 159: [10], 160: [9], 161: [9], 162: [7], 163: [7], 164: [10], 165: [9], 166: [8], 167: [8], 168: [10], 169: [8], 170: [7], 171: [9], 172: [9], 173: [10], 174: [9], 175: [9], 176: [8], 177: [9], 178: [8], 179: [7], 180: [7], 181: [9], 182: [10], 183: [9], 184: [10], 185: [10], 186: [10], 187: [10], 188: [9], 189: [8], 190: [10], 191: [10], 192: [9], 193: [7], 194: [10], 195: [10], 196: [8], 197: [8], 198: [9], 199: [10], 200: [9]}
Percentatge d'encerts en predicció iogurt mes valorat: 72.0 %
Percentatge d'encerts en prediccions dins dels 2 mes valorats: 86.0 %
```

### Activitat 5

Compareu els resultats de les activitats 2 i 4. Quin mètode funciona millor en aquest exemple? Quins altres avantatges té cada mètode respecte l'altre?

**Resposta**

En aquest exemple en algunes execucions s'han obtingut resultats millors amb l'activitat 4, l'activitat 2 amb Pearson dóna resultats inferiors en comparació amb l'activitat 4 (no sempre), i l'activitat 2 similitud euleriana quasi bé obté de forma diferenciada els pitjors resultats en comparació amb els anteriors resultats.

L'activitat 2 té menys complexitat computacional i és més senzilla en comparació amb l'activitat 4, no obstant en fer noves prediccions en l'activitat 2 s'han de repetir els càlculs mentre que en l'activitat 4 únicament cal classificar els valors nous en grups utilitzant els centrodides.

Però la diferència més significativa entre les dues activitats és que en l'activitat 4 s'agrupa als consumidors en grups segons les seves valoracions i aquesta informació pot resultar útil en altres estudis. En l'activitat 2 es calcula la predicció amb l'afinitat d'un nou client amb tots els clients d'entrenament.