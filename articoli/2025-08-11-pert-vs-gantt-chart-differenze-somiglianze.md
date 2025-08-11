# PERT chart vs. Gantt chart: due strumenti, due filosofie di pianificazione

Quando si parla di project management, ci sono due strumenti che compaiono regolarmente nelle discussioni di chi deve pianificare e monitorare progetti: la **PERT chart** e il **Gantt chart**. Entrambi hanno lo stesso obiettivo di fondo — fornire una rappresentazione visiva delle attività di un progetto e delle loro relazioni — ma lo fanno con logiche, punti di forza e limiti diversi.

Un **PMO** efficace deve saper scegliere quando usare l’uno, quando usare l’altro e, soprattutto, come integrarli per ottenere il massimo beneficio in termini di pianificazione, monitoraggio e comunicazione.

## Che cos’è una PERT chart?

**PERT** sta per *Project Evaluation and Review Technique* ed è una tecnica probabilistica che mira a stimare i tempi di completamento di un progetto considerando tre possibili scenari per ogni attività:

1. **Ottimistico** – il tempo minimo necessario se tutto fila liscio.
2. **Più probabile** – la stima realistica basata sull’esperienza.
3. **Pessimistico** – il tempo massimo in caso di problemi.

Queste stime vengono combinate con una formula statistica che attribuisce maggiore peso al tempo “più probabile” ma tiene conto anche delle altre due variabili. Il risultato è una durata media attesa per ciascuna attività.

La PERT chart rappresenta il progetto come un **diagramma di rete**: nodi (che possono rappresentare attività o eventi, a seconda della notazione usata) collegati da frecce che indicano le dipendenze.

## Due notazioni possibili: AoA e AoN

La PERT può essere disegnata secondo due logiche:

1. **Activity on Arrows (AoA)** – Le frecce rappresentano le attività, i nodi indicano gli eventi di inizio e fine. Supporta solo la dipendenza *Finish to Start*.
2. **Activity on Nodes (AoN)** – I nodi rappresentano le attività, le frecce le relazioni. Più flessibile perché supporta tutti i tipi di dipendenze (FS, SS, SF, FF).

Oggi la notazione AoN è la più diffusa perché consente di rappresentare progetti complessi in modo più leggibile.

## Vantaggi della PERT

1. **Gestione dell’incertezza** – Perfetta per progetti in cui le durate non sono note con precisione, come quelli di ricerca e sviluppo.
2. **Identificazione del percorso critico** – Evidenzia subito le attività che determinano la durata complessiva del progetto.
3. **Visione logica delle dipendenze** – Aiuta a capire l’ordine corretto delle attività prima ancora di fissare date esatte.

## Limiti della PERT

1. **Aggiornamento difficile** – In progetti con centinaia di attività, ridisegnare la rete a ogni cambiamento può diventare impegnativo.
2. **Enfasi eccessiva sul tempo** – Non tiene conto diretto di costi o risorse condivise tra progetti.
3. **Poco adatta alla fase esecutiva** – È uno strumento più da pianificazione iniziale che da controllo operativo quotidiano.

## Che cos’è un Gantt chart?

Il **diagramma di Gantt** rappresenta le attività su un **asse temporale**.  
Sull’asse verticale (Y) si elencano attività, sotto-attività e milestone, mentre sull’asse orizzontale (X) si traccia il calendario. Ogni attività è visualizzata come una barra la cui lunghezza indica la durata. Le relazioni tra attività sono mostrate con frecce, simili a quelle della PERT ma integrate direttamente nella sequenza temporale.

Oltre a tempi e dipendenze, un Gantt moderno può includere:

* **Baseline** per confrontare piano e avanzamento reale.
* **Assegnazioni di risorse** per monitorare carichi di lavoro.
* **Percentuali di completamento** per valutare progressi.

## Vantaggi del Gantt

1. **Visione temporale chiara** – Mostra subito in che periodo avviene ciascuna attività e quanto durerà.
2. **Monitoraggio quotidiano** – È lo strumento ideale per seguire l’avanzamento in fase di esecuzione.
3. **Gestione delle risorse** – Consente di vedere chi è assegnato a cosa e se ci sono sovraccarichi.

## Limiti del Gantt

1. **Meno efficace nella pianificazione incerta** – Richiede date precise già in fase iniziale.
2. **Progetti troppo grandi diventano ingombranti** – Rischio di “effetto lenzuolo” con grafici illeggibili.
3. **Aggiornamenti complessi senza software** – Se non si usa un tool moderno, ogni cambiamento può richiedere molto lavoro.

## Quando usare PERT e quando Gantt

* **PERT** è più utile nella **fase iniziale** del progetto, quando i tempi sono incerti e serve mappare le dipendenze per calcolare il percorso critico.
* **Gantt** è lo strumento principe nella **fase esecutiva**, quando le date sono note e serve monitorare l’avanzamento e gestire le risorse.

Le organizzazioni più mature non scelgono: **usano entrambi**. La PERT per disegnare la logica e calcolare il percorso critico, il Gantt per tradurre questa logica in un piano temporale dettagliato e aggiornabile.

## Integrazione in un contesto PMO

Un PMO che vuole il meglio dei due mondi può:

1. Costruire la rete PERT per definire le sequenze logiche e stimare la durata complessiva.
2. Convertire la rete in un Gantt per fissare le date e gestire risorse e avanzamento.
3. Usare software di Project Portfolio Management (come BigPicture, integrato con Jira) per avere entrambi i diagrammi aggiornati automaticamente.

## Rischi di una scelta sbagliata

Usare un Gantt quando le stime temporali sono ancora aleatorie può portare a piani irrealistici che saltano al primo imprevisto.  
Usare una PERT per seguire l’avanzamento quotidiano significa non avere sotto controllo lo slittamento delle date e l’impatto sui deliverable.

## Conclusione

Sia la PERT che il Gantt sono strumenti fondamentali, ma servono in momenti e con obiettivi diversi.  
Il bravo project manager — e a maggior ragione un PMO — non si limita a conoscerli: sa **quando usarli** e come integrarli per fornire al management e agli stakeholder una visione chiara, realistica e condivisa.

---

**Consiglio di lettura**  
*Managing Fuzzy Projects in 3D: A Proven, Multi-Faceted Blueprint for Overseeing Complex Projects* – Lavagnon Ika, Jan Saint-Macary (2023).  
Questo volume, scritto da uno dei più autorevoli esperti africani di project management, affronta in modo sistematico il problema dei progetti “fuzzy” — quelli caratterizzati da elevata incertezza, requisiti mutevoli e stakeholder con aspettative divergenti. Ika e Saint-Macary propongono un approccio a tre dimensioni che combina analisi logico-razionale, comprensione delle dinamiche umane e gestione delle variabili politiche e di potere.  

Il collegamento con l’uso di PERT e Gantt è diretto: la PERT aiuta a mappare le dipendenze e stimare scenari, mentre il Gantt traduce queste logiche in un piano temporale operativo. Il modello “3D” di Ika fornisce il quadro metodologico per decidere **quando** affidarsi a ciascuno strumento, **come** adattarli alle condizioni mutevoli del progetto e **come** mantenere il controllo anche in presenza di forte ambiguità iniziale.  

Chi gestisce portafogli complessi o progetti strategici, soprattutto in contesti multiculturali e politicamente articolati, troverà in questo libro non solo teoria, ma esempi concreti (dalla costruzione di infrastrutture globali a progetti di innovazione tecnologica) che mostrano come integrare strumenti tradizionali e approcci adattivi in un’unica strategia vincente.
