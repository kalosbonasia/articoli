# BigPicture: orchestrare contesti, non solo progetti

Ogni sistema complesso richiede una forma di regia. Non basta avere buone idee: serve un ambiente che ne favorisca l’emersione, strumenti adatti, condizioni condivise. Lo stesso vale per i progetti. Pianificare non significa scrivere una lista di cose da fare: significa creare un ecosistema dove le iniziative possano svilupparsi in modo coordinato, coerente, tracciabile. In questo senso, BigPicture non è solo un’app per la gestione del lavoro. È un ambiente per progettare ambienti.

Thomas Edison, spesso descritto come un genio isolato, in realtà sapeva circondarsi di contesti favorevoli. Non inventava da solo: costruiva laboratori, strutture, dinamiche collaborative. Non fu solo un inventore, ma un progettista di condizioni. BigPicture, se ben utilizzato, svolge oggi un ruolo analogo. Aiuta a progettare non solo i flussi operativi, ma le condizioni organizzative che rendono possibile l’innovazione continua.

## Dimensionare per comprendere: la prima responsabilità

Prima di decidere come usare BigPicture, occorre chiedersi quanto è grande il sistema con cui si lavora. Jira, come noto, è scalabile. Ma ogni istanza ha un peso, e ogni peso ha conseguenze. Atlassian propone un modello di dimensionamento basato su taglie (S, M, L, XL), considerando parametri come:

- numero di utenti;
- volume di issue attive;
- quantità di custom field;
- complessità dei workflow.

È un esercizio di consapevolezza, non di classificazione. Perché se un solo parametro è fuori scala — ad esempio una quantità eccessiva di issue mai archiviate — l'intera istanza può risultare rallentata. E BigPicture, che si appoggia a Jira per sincronizzare dati, ne risente immediatamente.

In molti casi ho consigliato interventi mirati: chiusura di progetti non più attivi, revisione dei permessi, riduzione di campi inutilizzati. Non si tratta di semplificare, ma di restituire ordine. Di fare spazio per rendere l’ambiente leggibile e performante.

## Sincronizzazione: regolare il battito del sistema

BigPicture sincronizza i dati con Jira. Sempre. E proprio questa sincronizzazione è il cuore pulsante del sistema. Ma se non è regolata con criterio, può diventare un fattore di congestione. Per questo è fondamentale configurare correttamente la sezione *Performance*, intervenendo su:

- frequenza di aggiornamento (ogni quanti secondi aggiornare i dati);
- modalità di elaborazione (semplice, ottimizzata, limitata);
- priorità delle code (box attivi vs inattivi);
- soglie di attività e timeout.

Ho lavorato su istanze con migliaia di utenti e decine di migliaia di task attivi. In simili contesti, la gestione della sincronizzazione non è un’opzione, è un prerequisito. Configurare bene il motore di sincronizzazione consente di ridurre il carico sul server, migliorare i tempi di risposta dell’interfaccia e garantire una user experience fluida anche sotto stress.

## Box e struttura: la forma è sostanza

BigPicture organizza il lavoro in box. Ogni box può rappresentare un progetto, un programma, una delivery unit. Ma la vera forza di questo sistema è che consente di costruire una gerarchia coerente tra questi elementi. E come ogni struttura, anche questa dev’essere progettata con una logica precisa.

Chi lascia i box attivi senza motivo, chi non archivia, chi non cancella test box dimenticati, introduce rumore nel sistema. E ogni elemento superfluo viene comunque sincronizzato. Mantenere ordinata la struttura dei box non è questione estetica: è una pratica operativa fondamentale.

All’interno dei box, la Work Breakdown Structure (WBS) — ovvero la struttura dei task — va costruita usando structure builder coerenti. Esistono tre principali modalità:

- *built-in*: Epic, Versione, Sprint;  
- *link-based*: relazioni tra issue;  
- *manuale*: identazioni visive non sincronizzate con Jira.

Non tutte sono compatibili tra loro. E alcune combinazioni generano conflitti o gerarchie inutilmente complicate. Chi conosce bene BigPicture sa che costruire una WBS non significa “fare la scaletta del progetto”, ma definire una semantica condivisa del lavoro.

## Allineare obiettivi e attività: l’uso avanzato degli OKR

BigPicture non è solo gestione operativa. Con il modulo *Objectives and Key Results (OKR)* è possibile collegare la strategia con l’attività quotidiana. In diversi progetti di trasformazione ho usato gli OKR non come semplice dichiarazione d’intenti, ma come leva per rafforzare la cultura dell’esecuzione.

Un esempio concreto: in una PMI del settore retail, l’obiettivo era espandere la presenza in un nuovo mercato. Abbiamo definito come *Key Results*:

- apertura di cinque sedi fisiche;
- raggiungimento di una soglia di 2.000 lead qualificati;
- aumento del traffico organico del 30%.

Questi risultati sono stati legati direttamente ad attività tracciate in Jira, visualizzate nel modulo Gantt e collegate alla roadmap. L’allineamento non era più un principio teorico, ma un meccanismo operativo tracciabile.

## Priorità come cultura, non come urgenza percepita

Uno dei problemi più diffusi è la mancanza di criteri chiari per stabilire le priorità. In molte aziende tutto è urgente, tutto è strategico, tutto è “da fare entro ieri”. BigPicture risponde con un modulo strutturato per la gestione delle priorità, basato su metodologie come:

- RICE (Reach, Impact, Confidence, Effort)
- ICE (Impact, Confidence, Ease)
- WSJF (Weighted Shortest Job First)

In contesti di revisione strategica ho utilizzato queste metriche per confrontare proposte, valutare il valore atteso, decidere in modo oggettivo su dove investire. Le priorità, una volta definite, vengono integrate nei piani e distribuite nei moduli operativi. Il passaggio da strategia a delivery avviene senza soluzione di continuità.

## Performance e visualizzazione: non tutto va mostrato

BigPicture permette di visualizzare molte cose. Ma non tutto va mostrato, e non tutto va caricato contemporaneamente. È importante:

- ridurre le colonne visibili nei moduli (massimo 10 per vista);
- limitare il numero di structure builder attivi in un box;
- usare filtri JQL semplici e ben scritti;
- disattivare i widget superflui sulla vista issue;
- archiviare regolarmente i box e i progetti Jira non più in uso.

La prestazione non è solo un dato tecnico: è un’esperienza di qualità. E la qualità si progetta. Anche qui, l’utente esperto sa distinguere tra ciò che serve davvero e ciò che distrae.

## BigPicture come ambiente di pensabilità operativa

Chi si limita a usare BigPicture come un “Gantt evoluto” non ne comprende la natura. Questo strumento non serve solo a pianificare: serve a pensare. Aiuta a costruire ambienti cognitivi in cui la complessità viene resa leggibile, le decisioni sono tracciabili e il lavoro assume una forma coerente.

Per questo BigPicture non è solo un prodotto. È una piattaforma che mette in relazione ruoli, strumenti, processi e responsabilità. E come ogni infrastruttura ben progettata, produce ordine dove prima c’era dispersione.
