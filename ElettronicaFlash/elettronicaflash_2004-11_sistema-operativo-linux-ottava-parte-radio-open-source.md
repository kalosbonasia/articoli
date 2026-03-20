# Sistema operativo Linux – ottava parte: Radio Open Source

**Autore:** Calogero Bonasia  
**Pubblicazione:** Elettronica Flash – linuxteam, novembre 2004  
**Licenza:** [CC BY-ND 4.0](https://creativecommons.org/licenses/by-nd/4.0/)

---

Basta davvero poco per trasmettere su Internet: grazie al contributo di alcuni appassionati è adesso possibile realizzare facilmente uno studio radiofonico.

Occorrono un server di trasmissione e un client per l'encoder (il codificatore) che possono anche stare su un unico calcolatore, sebbene sia preferibile separare i sistemi per ottenere il migliore risultato. Oltre al nome di dominio è bene dotarsi di una connessione con IP statico. Non che siano strettamente necessari, ma evitano di dover notificare di volta in volta agli ascoltatori l'IP dal quale trasmettiamo. Poiché in Italia è ancora costoso procurarsi una connessione T1 vi suggerisco di appoggiarvi ad un buon ISP che offra connettività di alta qualità.

Lo schema di principio della stazione radiofonica digitale prevede: la voce proveniente dai microfoni in formato analogico viene inviata ad un mixer che concentra il flusso verso il client dove risiede l'encoder costituito dal programma Liveice; mentre LAME si occupa della conversione da analogico a digitale della voce e degli altri ingressi. Il server di trasmissione esegue Icecast, che utilizzando un formato di trasmissione del flusso ed una porta TCP/IP convenzionalmente riconosciuta dai comuni riproduttori MP3 ci permetterà di spedire su Internet la nostra programmazione radiofonica.

L'aspetto più interessante è che processi differenti possono essere lanciati su calcolatori diversi configurati in maniera opportuna (ottimizzando ad esempio la connessione di rete, le regole di filtraggio, il carico sulla CPU) in modo che un servizio non inibisce l'altro.

Icecast è la controparte Linux del programma Shoutcast. Entrambi permettono di diffondere musica via Internet in tutto il mondo. Il formato musicale abitualmente impiegato per le trasmissioni è MP3 con un rateo dati di 32 o 64 kBps. I riproduttori MP3 memorizzano in un buffer di alcuni secondi i flussi da riprodurre provenienti da Internet, per sopperire ad eventuali piccole interruzioni. Il formato MP3 permette di ascoltare la programmazione musicale a chiunque abbia Xmms o Winamp.

A prescindere, ed è importante viste le ultime evoluzioni legislative proprio in Italia, la trasmissione al pubblico di materiale tutelato con i diritti d'autore va svolta nel pieno rispetto delle normative. Assicuratevi di avere il permesso per trasmettere i brani di cui non siete gli autori materiali.

## Installazione del server Icecast

L'installazione di Icecast non è particolarmente difficile. Per prima cosa occorre scaricare da Internet il programma, localizzato su http://icecast.linuxpower.org/. Scaricate la versione più recente e decomprimete il tutto:

```
tar zxvf icecast-1.x.x.tar.gz -C /tmp
cd /tmp/icecast-1.x.x/
```

Il programma va compilato digitando:

```
./configure
make
```

e come utente root installate il pacchetto:

```
make install
```

Questo comando copia tutti i file necessari al funzionamento su `/usr/local/icecast`. Il file di configurazione si trova in `/usr/local/icecast/etc/icecast.conf`.

I settaggi più importanti riguardano: la locazione del server, l'indirizzo email del responsabile, la porta (di default 8010), il nome del server, e le password per encoder, amministratore e operatore. Per lanciare il server per la prima volta (come root sulla porta 8010), digitate:

```
/usr/local/icecast/bin/icecast -P 8010
```

## Installazione di LAME e Liveice

L'installazione di Liveice è senza sorprese. Tuttavia, prima di iniziare occorre installare un codificatore MP3. Raccomando l'uso di Lame perché lavora egregiamente assieme a Liveice. Questo programma è reperibile all'indirizzo http://www.sulaco.org/mp3/. Dopo averlo scompattato, occorre compilare ed installare il pacchetto:

```
cd /tmp/lame3.87/
./configure
make
make install
```

Seguite la medesima procedura per Liveice (reperibile da http://star.arm.ac.uk/~spm/software/liveice.html):

```
tar zxvf liveice.tar.gz -C /tmp
cd /tmp/liveice
./configure
make
make install
```

Liveice può essere configurato tramite un'apposita interfaccia. Il file di configurazione si trova nella directory `/usr/local/liveice`. Impostate il formato PCM Audio a 32000Hz, selezionate l'encoder LAME3 con un rateo di 32000 bit e salvate la configurazione nel file `liveice.cfg`.

## L'input di linea

Il mixer fornisce una vasta gamma di opzioni per l'input. Durante la trasmissione si possono scegliere le sorgenti più diverse o i file MP3 già memorizzati sul disco fisso. Liveice richiede una qualità particolare per l'ingresso audio: se il volume di registrazione è troppo basso, non si sentirà nessun segnale in uscita; viceversa, se è troppo alto saturerà l'ingresso del mixer. Come nelle stazioni tradizionali, basterà ascoltarsi e regolare i valori per il risultato migliore. Come mixer software potete provare kmix, gmix o xqmixer.

## Trasmissione audio/video

Un possibile impiego alternativo consiste nell'inviare l'audio in abbinamento ad una sorgente video. Esistono numerosi documenti sulla rete e articoli apparsi sulle riviste specializzate che spiegano come predisporre un server per lo streaming video. Se diffondete le immagini di una web-cam il suono non è molto importante, ma cos'è una trasmissione televisiva senza audio?

Dal lato dell'ascoltatore occorre oltre al browser un qualsiasi riproduttore MP3 che sia interfacciabile ad Icecast (per esempio xmms, freeamp, mpg123):

```
mpg123 http://my.server.local:8010
```

La codifica in tempo reale è più efficiente rispetto alla semplice riproduzione di un file MP3, che invece soffre il ritardo di riproduzione e quindi si avverte la mancanza di sincronia tra audio e video.

## Riferimenti

- http://www.sulaco.org/mp3/
- http://star.arm.ac.uk/~spm/software/liveice.html
- http://www.icecast.org/
- http://www.opensourceradio.com
- http://www.mclink.it
- http://www.shoutcast.com
