# Sistema operativo Linux – nona parte: Aggregazione di banda con Linux

**Autore:** Calogero Bonasia  
**Pubblicazione:** Elettronica Flash – linuxteam, gennaio 2005  
**Licenza:** [CC BY-ND 4.0](https://creativecommons.org/licenses/by-nd/4.0/)

---

In alternativa all'ADSL, in molti contesti, si può ancora utilizzare la classica connessione ISDN.

L'installazione di ISDN, o la trasformazione di una linea normale, consiste nell'installazione di una presa terminale, di solito orrendamente chiamata "borchia" (per una quanto lontana similitudine con la forma delle prese telefoniche analogiche di una volta). Nella fornitura base (la cosiddetta BRI) sono previsti due canali dati a 64kbs (chiamati canali B1 e B2) ed un canale voce (chiamato D). In realtà il canale voce è un altro canale dati (8kb/s), che viene usato per la fonia.

Sulla borchia vi sono due prese alle quali potete collegare le apparecchiature ISDN, cioè telefoni, modem e schede di rete. Quello che non è sempre chiaro è che indipendentemente dal tipo di borchia installata avete sempre la divisione tra canali dati e canale fonia: mentre usate i canali dati per una connessione il telefono continua a rimanere disponibile.

Ad una fornitura base ISDN potete fare assegnare più di un numero di telefono, quelli che in termini tecnici vengono chiamati MSN. Quello che di solito il commerciale della compagnia telefonica non vi dice è che non serve avere due numeri di telefono per gestire in modo separato la fonia dalla trasmissione dati: il protocollo ISDN infatti distingue in modo autonomo le chiamate dati da quelle fonia, quindi un numero di solito basta ed avanza.

## Il protocollo PPP MultiLink

Vediamo quindi come è possibile unire i due canali in maniera dinamica ed omogenea sfruttando il protocollo PPP MultiLink tramite Linux. Questo metodo può essere applicato non soltanto alle linee ISDN (si possono aggregare anche più di due canali) ma anche alle linee analogiche o alle schede di rete Ethernet.

Per le schede di rete è preferibile utilizzare un sistema che permette di unificarle sotto un indirizzo IP virtuale (per esempio per aumentare la banda verso un server dipartimentale). Generalmente l'accesso ISDN viene fornito attraverso due canali di tipo B, che sono in grado di trasportare voce o dati in forma digitalizzata per un rateo massimo di 64 Kb/s.

Il protocollo PPP Multilink permette di connettere più canali con una tecnica che viene comunemente chiamata boundling (o link aggregation). Il vincolo sta nel fatto che dall'altro capo della linea il sistema con il quale vi collegate deve utilizzare anch'esso PPP Multilink.

Un'altra prerogativa del protocollo PPP Multilink è che durante il suo funzionamento non necessariamente vengono impegnati tutti i canali aggregati, ma questo varia in funzione della banda richiesta; cioè è possibile specificare una soglia, superata la quale, viene utilizzato anche il secondo canale e così via. Ad esempio, in un piccolo ufficio viene impiegato il PPP Multilink sul proprio proxy/firewall, per navigare su Internet; durante la normale attività ci si impegna su solo canale, ma se occorre scaricare un grosso file via FTP, si richiede più banda e quindi si attiva anche il secondo canale, in maniera del tutto trasparente agli utenti.

Personalmente ho adottato questo sistema per una scuola: ottimizzando così l'utilizzo dell'abbonamento Internet in funzione del numero di calcolatori che ne richiedevano l'accesso, consentendo un certo risparmio sulla bolletta del telefono. Nel caso particolare si trattava di un Istituto Scolastico ubicato in un territorio non servito da ADSL.

## Configurazione

I file di configurazione si trovano sotto `/etc`, come è risaputo. Quelli che riguardano il setup della scheda ISDN, se utilizziamo SuSE Linux sono posizionati sotto `/etc/isdn`, mentre se utilizziamo Linux Redhat, sono sotto `/etc/sysconfig` (isdncard e ifcfg-ippp0).

Esaminando nel dettaglio il file di configurazione del protocollo PPP, si nota:

```
# /etc/sysconfig/network-scripts/ifcfg-ippp0
[omissis...]
ENCAP = syncppp   (indica di instaurare una connessione sincrona)
BUNDLING = off    (indica che per ora il bundling è disattivato)
```

Per attivare il secondo canale B, il parametro da modificare è appunto `BUNDLING`, sia tramite riga di comando che mediante le più comode interfacce grafiche. Nel file `/etc/sysconfig/network-scripts/ifcfg-ippp0` avremo quindi:

```
BUNDLING=on e SLAVE_DEVICE = ippp1
(che indica il device associato al secondo canale B)
```

L'allocazione dinamica della banda (quindi il numero di canali B utilizzati in contemporanea) viene gestita dal demone ibod, che significa ISDN MPPP bandwidth on demand, il cui file di configurazione è `/etc/isdn/ibod.cf`. In particolare:

- `ENABLE` è il parametro che gestisce l'attivazione della banda su richiesta
- `INTERVAL` definisce l'intervallo di tempo complessivo prima dell'attivazione o disattivazione del device slave (predefinito è di 5 secondi)
- `LIMIT` riguarda una eventuale limitazione di banda per attivare l'uso dei canali supplementari

Riassumendo: se 128 Kb/s non bastano è possibile aggregare anche più canali ISDN per ottenere maggiore larghezza di banda, anche nel caso il nostro provider non supporti pienamente il protocollo PPP Multilink. Occorrerà fare in modo che più canali fisici di tipo B appaiano come un unico collegamento logico.

## Bilanciamento del carico con Ethernet bonding

Per effettuare il bilanciamento di carico occorre modificare la route di default gateway che di solito è impostata sulla prima interfaccia isdn (ippp0), come segue:

```
ip route add default scope global equalize nexthop dev ippp0 nexthop dev ippp2 nexthop dev ippp4
```

La parola chiave `nexthop` è quella che dice al sistema di "equalizzare" le route su tutte le interfacce attive dichiarate (quelle di numero dispari, come detto non occorre dichiararle, perché slave e gestite in automatico dallo script sotto `/etc/sysconfig`).

Infine, come detto all'inizio dell'articolo, se al posto delle interfacce ISDN utilizzassimo delle particolari schede di rete Ethernet che supportano un unico indirizzo IP virtuale, si potrebbe adottare una tecnica conosciuta come "bonding" che aggrega a livello logico tutte le porte delle schede in uso sul sistema, come se fossero una soltanto, sommando la banda di ciascuna. Un impiego tipico è quello di aumentare banda verso un server dipartimentale cui accedono numerosi client (per esempio per trasferimento di grossi file audio o video).

In futuro torneremo ancora sulle applicazioni di Linux nel settore della telefonia per vedere ad esempio come sia possibile costruire un centralino telefonico interamente basato su Linux e schede ISDN.

## Riferimenti

- RFC 1990 e RFC 1717 (sul protocollo PPP Multilink)
- http://trieste.linux.it/documenti/Italian-ISDN-Mini-HOWTO.php (una guida che spiega come collegare Linux ad Internet mediante ISDN)
