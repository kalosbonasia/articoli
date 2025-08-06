# BigPicture: governare la struttura, comprendere la complessità

Quando, più di dieci anni fa, iniziai a introdurre BigPicture nei contesti aziendali italiani, era un tempo in cui il concetto stesso di *project portfolio management* era spesso frainteso o ridotto a una lista di progetti in Excel. Da allora, ho accompagnato decine di organizzazioni, consulenti, product owner e PMO nel comprendere e adottare questo strumento. Non come semplice plugin di Jira, ma come grammatica organizzativa.

BigPicture non è un’app da installare e dimenticare. È un sistema che impone un cambiamento culturale. Oggi, grazie alla versione Enterprise, le sue potenzialità si sono ulteriormente ampliate, ma i problemi di fondo restano sempre gli stessi: come strutturare bene, come dare senso ai dati, come costruire una visione leggibile della complessità.

In questo articolo, riassumo i concetti fondamentali da conoscere per usare BigPicture in modo consapevole. È il frutto di anni di esperienza sul campo, nelle aziende italiane, a fianco di chi progetta e di chi decide.

## I box: unità semantiche di lavoro

In BigPicture tutto parte dai *box*. Sono spazi contenitori che possono rappresentare un progetto, un programma, un'iniziativa Agile, una roadmap o persino un'interazione singola. Ogni box ha una struttura, dei moduli attivi e una serie di configurazioni. Non è un contenitore vuoto: è una cellula organizzativa, dotata di identità.

Grazie ai *box type* – undici nella versione standard, illimitati in Enterprise – è possibile creare template pronti all’uso per Agile, Waterfall o approcci ibridi. Il PMO può definire standard condivisi, riducendo l’improvvisazione e assicurando coerenza tra le unità di lavoro. Ogni box può inoltre ereditare parametri da quelli superiori, permettendo un governo multilivello del portafoglio.

## Gerarchie: task e box parlano la stessa lingua

BigPicture permette di definire due tipologie di gerarchia:

- **Task hierarchy**, ovvero la struttura a n livelli dei task all'interno di un box. Si basa su *identazioni*, link di parentela (Epic, Versione, Sub-task) e *basic tasks* aggregatori. Le identazioni visive possono essere illimitate, e i basic task aggregano dati da quelli figli: stato, effort, costi.

- **Box hierarchy**, ovvero la struttura gerarchica dei box stessi. Un Agile project può contenere Iteration boxes, che a loro volta contengono task. A livello superiore, un Program box o un Portfolio box possono aggregare più progetti. Questa struttura ad albero consente di leggere l’organizzazione nella sua profondità.

In entrambi i casi, ciò che conta non è solo la forma, ma il significato: ogni gerarchia è un modello operativo implicito. Costruirla bene significa dare senso al lavoro.

## Dipendenze: forti, deboli, ma sempre esplicite

BigPicture distingue tra **strong dependencies** e **soft dependencies**:

- Le *strong* hanno impatto sullo scheduling. Se il task A finisce il 2 aprile, il task B collegato (end-to-start) non potrà iniziare prima. Con l’autoscheduling attivo, BigPicture aggiorna automaticamente le date.

- Le *soft* sono invece informative: mostrano relazioni, ma non influenzano la pianificazione.

È una distinzione cruciale, soprattutto quando si lavora su più livelli. Le dipendenze forti aiutano a mantenere coerenza temporale, le soft aiutano a comprendere la logica del flusso.

## Stime e date: due prospettive sul tempo

Ogni task può essere stimato in termini di tempo o story points. BigPicture gestisce due valori fondamentali:

- **Original Estimate**, la previsione iniziale del tempo necessario  
- **Remaining Estimate**, il tempo residuo aggiornato in base al *Time Spent*

Queste stime si incrociano con le **date programmate** (start e end date), che possono essere definite manualmente, assegnate tramite drag & drop o lasciate vuote finché il task non è pronto per essere schedulato.

Tutti i task non schedulati appaiono in un pannello dedicato nel modulo Resources: niente viene perso, ma nulla viene anticipato senza decisione.

## Risorse: workload e capacità

La gestione delle risorse in BigPicture si fonda sulla distinzione tra:

- **Workload**: la somma dell’effort assegnato a una risorsa in un intervallo di tempo  
- **Capacity**: la disponibilità teorica, calcolata in base al piano di lavoro (es. 8h/giorno), alle ferie, alle assenze e alla percentuale di coinvolgimento nel progetto

Nel modulo Resources è possibile visualizzare queste informazioni con indicatori grafici: sovraccarichi, saturazioni, sotto-utilizzi. BigPicture permette di lavorare per persona, per team o per ruolo, adattandosi ai diversi modelli organizzativi.

## Team basati su gruppi Jira (Enterprise)

Con BigPicture Enterprise è possibile creare team a partire da gruppi Jira esistenti. La procedura è semplice:

1. Si seleziona "Crea team da gruppo Jira"  
2. Si sincronizzano i membri (operazione manuale)  
3. Si definisce la disponibilità iniziale dei membri (default 100%)

Il vantaggio? Non serve più ricostruire a mano i team per ogni progetto. È sufficiente creare il team nel box radice (Home) e assegnarlo ai box inferiori. La sincronizzazione mantiene aggiornato il team in base ai cambiamenti del gruppo Jira, ma solo nel box in cui viene effettuata.

## Scenari ipotetici: pensare prima di agire

Il modulo *What-if scenarios* permette di simulare variazioni senza toccare il piano reale. Nella versione base si possono creare due scenari per progetto. In Enterprise, il limite scompare: è possibile generare versioni alternative, confrontarle, stressarle.

È una funzione preziosa in fase di negoziazione interna, rilascio di roadmap o revisione dei piani. Si può ragionare in modalità “e se?” senza rischiare impatti indesiderati.

## Reporting: visione, non solo dati

Jira offre molti report, ma si ferma al livello del singolo progetto. BigPicture va oltre, introducendo un vero e proprio **modulo Reports** che copre:

- conteggio task e stato di avanzamento  
- matrice dei rischi  
- dipendenze tra team

Con Enterprise si aggiungono report su:

- milestone e marker  
- capacità e workload aggregati  
- ritardi rispetto ai baseline  
- velocity su più sprint

Ogni report può essere filtrato via JQL, visualizzato in dashboard modulari, personalizzato su più livelli. È possibile esplorare dati in profondità: da un indicatore generale si può arrivare fino al dettaglio per assignee, per priorità, per status.

Il risultato? Un sistema di reporting multilivello che integra visione e controllo.

## Conclusione: la differenza tra usare e comprendere

Chi adotta BigPicture oggi trova uno strumento potente e maturo. Ma chi lo ha introdotto quando ancora non esisteva una cultura della portfolio governance, ha dovuto affrontare problemi ben più strutturali: confusione metodologica, assenza di strategia, cattivo uso degli strumenti.

Essere stati i primi significa aver imparato molto, anche dagli errori. Nel mio caso, significa oggi saper distinguere tra chi usa BigPicture e chi lo comprende. La differenza è sottile, ma decisiva. E si vede nei risultati.
