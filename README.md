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

### Activitat 2

Prenent les dades del fitxer d'entrenament, genereu un recomanador ponderat de iogurts nous pels consumidors de prova (identificadors 101..200), de manera que a cadascun d'aquests consumidors se li recomani quin dels nous iogurts l'hauria d'agradar més tenint en compte les valoracions dels consumidors d'entrenament (1..100). Proveu amb similitud euclidiana i amb correlació de Pearson com a mides de similitud.

Seguidament, compareu la recomanació feta per cada usuari (serà un dels iogurts 7..10) amb les seves valoracions enregistrades al fitxer de validació. En quin tant per cent dels casos la recomanació coincideix amb una valoració de 5? I de 4? Quines conclusions es poden treure?

Compareu les diferències (si hi ha) entre les recomanacions amb similitud euclidiana i amb correlació de Pearson.

### Activitat 3

Genereu un dendrograma pel mètode aglomeratiu que faci l'agrupament dels consumidors fent servir només les dades del fitxer de prova. No cal generar el diagrama d'arbre, només ens interessen els grups generats.

Hauríeu d'obtenir una sèrie d'agrupaments de consumidors; preneu com a resultat l'agrupament en el qual queden exactament quatre grups. Ara accediu al fitxer de validació i determineu quin és el iogurt més valorat per cada usuari. Associeu aquesta informació amb els grups obtinguts amb el dendrograma: els grups són uniformes a les seves valoracions dels nous iogurts? És a dir, quin tant per cent de cada grup prefereix el mateix iogurt (dels nous)?

Podeu comparar els resultats fent servir els diferents mètodes d'enllaç que hi ha als materials de l'assignatura.

### Activitat 4

Feu servir l'algorisme k-means (el teniu al codi 4.4 dels materials) per generar quatre grups de consumidors tenint en compte només les valoracions dels iogurts 1..6 dels consumidors del fitxer d'entrenament.

Com a resultat obtindreu quatre grups de consumidors amb valoracions semblants i quatre centroides, és a dir quatre consumidors representatius de cadascun dels quatre grups.

Calculeu quin és el nou iogurt preferit (valoració igual a cinc) de cada grup. És el mateix que el preferit pel seu centroide? Per qué?

A continuació farem servir els centroides obtinguts com a recomanador basat en models per nous consumidors. Determineu a quin grup pertany cadascun dels consumidors del fitxer de prova, i com a conseqüència quin nou iogurt li recomanaríeu.

Compareu aquesta recomanació amb la seva pròpia valoració registrada al fitxer iogurts_validacio.data. Quin tant per cent d'encert s'obté (usuaris als que s'hi recomana el seu nou iogurt preferit)? I si relaxem una mica les condicions, és a dir acceptem per bona una recomanació dels iogurts amb valoració 4 o 5, quin tant per cent d'encert s'obté?

### Activitat 5

Compareu els resultats de les activitats 2 i 4. Quin mètode funciona millor en aquest exemple? Quins altres avantatges té cada mètode respecte l'altre?