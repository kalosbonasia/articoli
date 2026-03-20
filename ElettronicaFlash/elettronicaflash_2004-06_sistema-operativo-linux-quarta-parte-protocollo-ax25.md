# Sistema operativo Linux – quarta parte: Protocollo AX.25

**Autore:** Calogero Bonasia  
**Pubblicazione:** Elettronica Flash – linuxteam, giugno 2004  
**Licenza:** [CC BY-ND 4.0](https://creativecommons.org/licenses/by-nd/4.0/)

---

Linux è forse l'unico sistema operativo che offre un supporto nativo standard per il protocollo AX.25, utilizzato in tutto il mondo dai radioamatori per il packet radio.

L'implementazione in Linux dei protocolli di rete per radioamatori è molto flessibile, ma per coloro che non hanno particolare familiarità con questo sistema operativo il processo di configurazione può apparire complesso e laborioso; infatti occorre un po' di tempo per capire tutto l'insieme. Configurare il proprio sistema può risultare un'operazione molto difficile se non ci si è prima documentati sul funzionamento di Linux in generale.

Il protocollo AX.25 offre la possibilità di lavorare o meno in modo connesso, ed è usato sia da solo in collegamenti punto-punto, che come trasporto per altri protocolli come il TCP/IP e NET/ROM. La sua struttura è simile all'AX.25 livello 2, con alcune estensioni che lo rendono più adatto all'ambito radioamatoriale. Il protocollo NET/ROM rappresenta un tentativo di realizzare un protocollo di rete completo e usa AX.25 al livello più basso come protocollo dati. Presenta uno strato di rete che è una forma adattata di AX.25 e offre il routing dinamico e l'alias dei nodi.

Come al solito vi suggerisco di approfondire il tema leggendo "AX-25 How To", disponibile sia nella versione originale di Jeff Tranter VE3ICH, che nell'ottima traduzione a cura di Nico Alberti e Michele Ferritto, reperibile su `pluto.linux.it` (precisamente all'indirizzo internet: http://ildp.pluto.it/HOWTO/AX25-HOWTO/index.html).

Quella in Linux è un'implementazione dell'AX.25 del tutto nuova. Sebbene assomigli in molti modi a quella di NOS, BPQ o altre implementazioni AX.25, non è uguale a nessuna di queste. L'AX.25 di Linux è in grado di essere configurato in modo tale da poter comportarsi praticamente come le altre implementazioni, ma il processo di configurazione è del tutto diverso.

## Installazione del supporto AX.25

Per installare correttamente il supporto per AX.25 sulla vostra macchina Linux, occorre configurare ed installare un kernel appropriato e poi installare le utilità AX.25. Selezioniamo quindi tramite YaST: `ax25-apps`, `ax25-doc` (che contiene la documentazione), `ax25spyd` (il demone di monitoraggio) e gli `ax25-tools`. Se preferite, installate pure `fpac`, che è un'applicazione dedicata per trasformare la vostra macchina in un nodo X.25, e `axw3`, un programma che permette di richiamare pagine web da Internet direttamente mediante AX.25.

## Il TNC e l'interfaccia dati

Usualmente è il cosiddetto TNC (Terminal Node Controller) che svolge la funzione di vero e proprio sistema autonomo per il Packet Radio; sarebbe infatti possibile avere uno stupido terminale seriale, collegarci il TNC, ed iniziare a fare Packet Radio: il TNC si prenderà cura di gestire il protocollo AX.25, il modem a lui collegato provvederà a pilotare la ricetrasmittente.

Il problema che rende l'uso dei comuni TNC inadeguato per l'impiego ad alte velocità è il fatto che essi si interfacciano attraverso la porta seriale. Tuttavia le comunicazioni seriali, per loro natura essenzialmente asincrone, soffrono dell'uso intensivo di interrupt sia per il computer che per il TNC stesso; la velocità massima raggiungibile è comunque non superiore a poco più di 100kbit/sec.

Il TNC2, il modello più diffuso nella comunità radioamatoriale, è controllato da un semplice Z80 che, al massimo, raggiunge i 10MHz. Ciò, sperimentalmente, ha limitato l'uso di TNC2 alla velocità max di 19200 baud. Su molti siti dedicati al packet-radio si parla di un'interfaccia, la PI2, la quale, così come altre schede del genere, ci viene in aiuto proprio dove il TNC perde il terreno conquistato negli anni: la velocità. Il fatto di potersi principalmente avvalere di trasferimenti non-interrupt-driven porta la velocità supportata fino ad almeno 250kbit/sec. Per le schede Ottawa PI-2 Card, ci si può rivolgere solo a chi le ha costruite e farsele spedire. Il loro costo si aggira intorno ai 150,00 euro, I.V.A. e sdoganamento inclusi.

## Configurazione della porta AX.25

La configurazione della porta "A" non è molto diversa da una normale interfaccia di rete. Basterà impartire il comando:

```
# ifconfig pi0a hw ax25 IW9CUK-3 up
```

Questo comando assegna il nominativo IW9CUK-3 alla porta ad alta velocità alla prima PI-2 Card rilevata e la rende attiva. Il passo successivo è quello di far trasportare il TCP/IP dall'interfaccia in AX.25 appena attivata:

```
# ifconfig pi0a 144.134.84.77 netmask 255.255.255.0 broadcast 144.134.84.255
# route add -net 144.0.0.0 pi0a netmask 255.0.0.0
# route add default pi0a
```

Il primo comando assegna alla porta appena configurata l'indirizzo IP mostrato (che è del tutto inventato; ripeto, per indirizzi validi, contattate il responsabile IP della vostra zona), con le usuali netmask e broadcast address per una rete IP di classe C. Il secondo aggiorna la tabella di routing del kernel per far sì che ogni indirizzo della sottorete 144.0.0.0 sia instradata all'interfaccia radio.

A questo punto si può provare con un classico `ping` se tutto funziona, o con un più attraente `ssh` o `telnet` o, perché no, con Mozilla.

## Software per meteor scatter

Per chi fosse appassionato del DX in onde corte o microonde, segnalo JT44 e FSK441. Sono due programmi specifici per il meteor scatter. JT44 in particolare è sovente impiegato per il EME (moonbounce) e il troposcatter, perché in grado di decodificare velocemente anche segnali molto deboli. Al solito, potete installarli mediante YaST, oppure scaricarli da www.qsl.net/g4klx/software.htm.

## Riferimenti

- www.afthd.tu-darmstadt.de/dg1kjd/linux-ax25/index.html
- www.tldp.org/HOWTO/AX25-HOWTO/x2329.html
- http://home.snafu.de/wahlm/dptnt.html
- http://sourceforge.net/projects/hams/
- http://freshmeat.net/projects/ax25-apps/
- http://freshmeat.net/projects/libax25/
- http://sourceforge.net/projects/ghu/
- www.irlp.net/
- ftp.kernel.org (sorgenti del kernel)
- ftp.pspt.fi (aggiornamento AX.25)
