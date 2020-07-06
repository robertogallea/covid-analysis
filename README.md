# Linee guida per la realizzazione del progetto di fine corso

Il progetto di fine corso deve avere la forma di un pacchetto python (anche non installabile),ovvero deve essere composto da uno o più moduli (file .py) e deve rispettare i seguenti requisiti:
1. Fornire una funzionalità nella forma di una funzione o di un metodo che permetta di scaricare uno o più dataset tramite una API o una richiesta ad una JSON API;

    a. [Opzionale]​ Fornire una funzionalità nella forma di una funzione o di un metodo che permetta di salvare i dati scaricati in un file locale con nome e percorso forniti come parametro;
    
    b. [Opzionale richiede 1.a] ​Fornire una funzionalità nella forma di una funzione o di un metodo che permetta di leggere il dataset da un file locale con nome e percorso fornito come parametro, e formato assunto uguale a quello utilizzato per il salvataggio al punto 1.a;

2. Fornire una funzionalità nella forma di una funzione o di un metodo che permetta (ad esempio con l’ausilio di un file) la memorizzazione permanente della configurazione per l’accesso allo strumento utilizzato per la memorizzazione dei risultati delle analisi. Lo strumento per l’archiviazione dei risultati potrà essere un file di testo o un database:

    a. nel caso in cui si scelga un database i parametri saranno quelli necessari alla connessione al database;
    
    b. nel caso in cui si scelga un file questi saranno il percorso ed il nome del file;

3. Fornire una o più funzionalità nella forma di funzioni o di metodi che consentano di selezionare diversi sottoinsiemi di dati a partire dal dataset di cui al punto 1 in base a criteri da stabiliti dall’autore del progetto;

4. Fornire una funzionalità nella forma di una funzione o metodo che consenta di effettuare una semplice analisi sul sottoinsieme di dati selezionato utilizzando le funzionalità di cui al punto 3. Il risultato di tale funzione o metodo deve essere un dizionario o una classe definita dall’utente strutturata in maniera tale da rendere esplicito il significato dei valori contenuti. L’analisi deve comprendere almeno tre differenti valori di aggregazione, a titolo di esempio:

    a. percentuali;
    
    b. medie aritmetiche;
    
    c. minimo e/o massimo valore;

5. Fornire una funzionalità nella forma di una funzione o di un metodo che consenta di salvare i risultati dell'analisi attraverso lo strumento stabilito al punto 2:

    a. Nel caso in cui si usi un file, il programma deve gestirne la creazione quando necessario ed essere in grado di appendere i risultati di ogni nuova analisi su una nuova riga, utilizzando il formato csv e di associare a ciascuna entry un identificatore univoco (ad esempio la data e orario in cui si è effettuato ilsalvataggio) o un identificatore passato come argomento opzionale dall’utente;
    
    b. Nel caso in cui si usi un database i risultati possono essere una nuova entry in una tabella o un nuovo documento json se usate un db non relazionale, anche in questo caso uno dei campi della tabella o la chiave del documento deve essere un identificatore univoco eventualmente definibile dall’utente;

6. Fornire una o più funzionalità nella forma di metodi o funzioni per produrre una o più tipologie grafici relativi al sottoinsieme di dati selezionato al punto 2 edeventualmente ai risultati delle analisi di cui al punto 4;
7. Fornire uno jupyter notebook di esempio (possibilmente annotato tramite markdown) in cui importando esclusivamente i file .py che compongono il progetto e, se opportuno, moduli della libreria standard di Python si dimostrino le differenti funzionalità implementate.