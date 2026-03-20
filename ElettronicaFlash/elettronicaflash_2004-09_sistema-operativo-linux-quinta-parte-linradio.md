# Sistema operativo Linux – quinta parte: Linradio!

**Autore:** Calogero Bonasia  
**Pubblicazione:** Elettronica Flash – linuxteam, settembre 2004  
**Licenza:** [CC BY-ND 4.0](https://creativecommons.org/licenses/by-nd/4.0/)

---

Quando le comunicazioni telefoniche e radio assumono una importanza vitale per i vostri affari o per situazioni di emergenza e sicurezza, allora diventa essenziale poterle documentare in modo affidabile e preciso.

La ricostruzione di eventi basati su conversazioni telefoniche e radio non può essere chiarita in modo affidabile da appunti scritti e dichiarazioni di persone che, in caso di disputa, raramente coincidono. La registrazione delle comunicazioni, con associazione di data/ora/minuto/secondo, diventa fondamentale per chiarimenti, verifiche, analisi e trascrizioni. Ero rimasto deluso dal fatto che alcuni dei principali costruttori di apparecchiature radio riceventi per radioamatori avessero a listino delle interessanti schede da installare direttamente sul calcolatore o da collegare esternamente via porta seriale, ma erano dotate solo di software per la piattaforma Windows.

Così, ricordando che lo scorso anno su questa rivista sono apparsi due articoli sui ricevitori digitali della Winradio (www.winradio.com), ho approfondito l'argomento per trovare una soluzione ad una richiesta che mi era stata sottoposta da un ente governativo: un progetto in cui si intendeva utilizzare un mixer audio per Linux. Nel mio caso ho utilizzato Glame, reperibile su sourceforge.net.

## Il supporto Linux per le schede Winradio

Con piacere ho scoperto il sito www.linradio.com. Tra i prodotti commercializzati vi è anche un sistema multicanale, rivolto agli enti governativi e militari, adatto alla sorveglianza e per la sicurezza di aree di interesse operativo. Questo sistema ha sei canali indipendenti, ed un range di frequenza da 150 KHz a 1500 MHz estendibile fino a 4 GHz. I segnali ricevuti possono essere registrati su disco rigido e richiamati tramite file. Le registrazioni includono il tempo, la data e le informazioni sulle trasmissioni ricevute. Sul sito è possibile trovare non solo software già pronti all'uso, ma, come è nello spirito dei radioamatori e degli utenti della comunità open source, è pure possibile contribuire direttamente allo sviluppo di software per queste schede.

Con il **Linradio Toolkit 0.4** di Pascal Brisset è possibile controllare appieno i ricevitori WR-1000i, WR-1500i, WR-3150i e i WR-1500e mediante qualsiasi calcolatore con installato un Linux per processori x86 (in sostanza Intel e AMD). Con i comandi:

```
# ./tclradio
% winradio wr 0x180
% wr -p 1 -f 100e6 -m FMW -a 0 -u 0 -v 50
```

è possibile fare rilevare alla linux box la scheda ricevente e subito dopo è possibile lanciare il programma di controllo, scrivendo `./wrpanel.tcl`.

Il programma **wrkit 0.1** aggiunge un misuratore di segnale al software di controllo della scheda ricevente. Il programma di Pascal Brisset è derivato da un programma che non sfrutta una GUI (una interfaccia grafica a finestre simile a quella di Windows), ma utilizza l'interfaccia terminale (quella tipo "DOS"), scritto da Yuri Muzyka. È comodo per chi volesse utilizzare anche un vecchio calcolatore con poca memoria RAM insufficiente per pilotare magari un ambiente grafico, oppure per pilotare da remoto un ricevitore, mediante una comune connessione telnet o SSH. Teoricamente potreste persino utilizzare un computer palmare della serie PALM: si tratta solo di "programmare".

## Il "./" davanti ai nomi dei programmi

In Linux non si utilizzano le estensioni per assegnare la proprietà di esecuzione di un programma, come per Windows (ad esempio `office.exe`), quindi anche uno script come `pippo.bau` potrebbe essere un programma ed essere eseguito con `./pippo.bau`.

## Sviluppo futuro e strumenti aggiuntivi

In futuro è prevista l'aggiunta di una funzione per il database delle frequenze, direttamente nel pannello di controllo del Toolkit, e la possibilità di registrare direttamente le comunicazioni ricevute per poterle riascoltare in un secondo momento con un qualsiasi player.

Per chi volesse cimentarsi nella sperimentazione e programmare queste schede, è possibile scaricare dal sito www.winradio.com diversi strumenti di sviluppo e molta documentazione tecnica, per realizzare sia semplici interfacce di controllo (per DOS, Windows, o appunto Linux) sia moduli per integrare le schede Winradio al famoso programma LabView. Mentre sul sito http://xrs.winradio.com/ trovate un approfondimento sulla piattaforma standard per realizzare sistemi riceventi controllati a distanza. Un ambiente di sviluppo comodo da utilizzare lo trovate anche su http://www.rbasic.com/.

Un particolare ringraziamento va al sig. Grandicelli, l'importatore italiano (www.grandicelli.com) che mi ha messo a disposizione il suo tempo e la documentazione tecnica su questi versatili ricevitori.

## Riferimenti

- www.linradio.com
- www.winradio.com
- http://xrs.winradio.com/
- http://www.rbasic.com/
- www.grandicelli.com
