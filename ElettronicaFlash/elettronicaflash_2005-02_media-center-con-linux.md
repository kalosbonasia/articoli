# Media center con Linux

**Autore:** Calogero Bonasia  
**Pubblicazione:** Elettronica Flash – linuxteam, febbraio 2005  
**Licenza:** [CC BY-ND 4.0](https://creativecommons.org/licenses/by-nd/4.0/)

---

Un nuovo modo di guardare la TV, padrone dei tuoi programmi televisivi, libero dalle incombenze degli orari e delle vecchie videocassette; un'alternativa per assaporare il piacere di ascoltare e vedere con l'assoluta qualità digitale audio video: l'ideale per avere tutto in un solo prodotto.

Circa un anno fa ho prestato la mia consulenza per un famoso hotel di Roma in merito all'analisi di alternative possibili e disponibili sul mercato per sostituire il loro sistema di pay-tv disponibile nelle camere degli ospiti. In commercio esistono soluzioni più o meno valide, le meno recenti basate su una distribuzione del segnale in modalità analogica e unità di controllo remoto piazzate nei televisori, le più recenti ovviamente fanno uso del segnale digitale, e permettono pure di gestire l'accesso ad Internet o a consolle di videogiochi, eccetera.

La piattaforma sulla quale si basano questi sistemi di solito è proprietaria e ovviamente "chiusa". Così come il sistema di Microsoft (Windows Media Center) recentemente presentato al FuturShow di Milano. Esistono tuttavia soluzioni basate su Linux, sia di tipo "commerciale" sia di tipo "open".

## TiVO: la tv-box basata su Linux

TiVO è forse la più famosa applicazione di una "tv-box" basata su Linux. Si noleggia una TiVO-Box (299 dollari per un noleggio "a vita"), si paga un canone mensile e si accede alla programmazione mediante una connessione a larga banda. Il sistema permette la registrazione fino a 140 ore di programmazione televisiva, ma permette anche di trasferire i contenuti sul vostro pc e viceversa, oppure di creare il vostro DVD personalizzato.

Esistono per la verità anche degli elettrodomestici di note marche del settore che permettono di masterizzare su DVD il contenuto preregistrato su hard disk relativo alla programmazione televisiva, una sorta di video registratore rivisitato, che al posto dei nastri "VHS" utilizza i DVD o l'hard disk.

## Windows Media Center: una breve premessa

Windows XP MCE è molto simile alla versione Professional di Windows XP, alla quale aggiunge un'interfaccia graficamente semplice e molto intuitiva che consente di utilizzare le varie funzioni multimediali tramite l'utilizzo di un semplice telecomando. Lo scopo di Windows Media Center è rendere il computer il centro dell'intrattenimento domestico, offrendo la capacità di registrare gli spettacoli televisivi, visualizzare immagini e video e riprodurre la musica.

Nei paesi in cui Windows MCE era già disponibile, la situazione si è evoluta in modo diverso dai desideri di Microsoft: fin dall'inizio sembrava che Media Center fosse soltanto un Windows XP caratterizzato dall'aggiunta di un nuovo menu. Non è però possibile acquistare Windows MCE sotto forma di pacchetto indipendente, in modo da poter creare un proprio Pc.

## MythTV: la soluzione open source

Partendo dal sito http://www.mythtv.org/ è possibile trovare un ottimo software che permette funzionalità "live-tv", con avanzamento, riavvolgimento e fermo immagine digitale, supporto per schede video e di acquisizione multiple per registrazione in contemporanea di più programmi. È anche possibile distribuire l'architettura della riproduzione dei contenuti (non solo video, ovviamente, ma anche audio) ad esempio per utilizzi in comunità, scuole o alberghi.

Un esempio di applicazione commerciale basata su questo software è reperibile sul sito http://www.dreamux.it/, dove Leandro Dardini ci spiega come funziona la sua "scatola dei sogni" per vedere foto e video e ascoltare musica o giocare. Con il capiente hard disk (fino a 600 GB di capacità equivalenti a 600 ore di registrazione) non si hanno più problemi a registrare il proprio programma preferito senza perdita di qualità.

I requisiti minimi per fare funzionare MythTV comprendono: un qualsiasi personal computer equipaggiato con un AMD Athlon XP 1800+, una scheda televisiva (le ATI ancora non lavorano del tutto bene con Linux), il database MySQL per memorizzare le informazioni di programmazione, la libreria FreeType (libfreetype versione 2) e le librerie QT in versione 3.0 o più recente.

## GeexBox

GeexBox (http://www.geexbox.org/) è un altro programma che permette di costruire una linux box capace di gestire contenuti multimediali in maniera semplice ed intuitiva. Supporta le principali schede video VESA 2.0 compliant (ad esempio le ATI Rage, ATI RageMobility, le nVidia Riva TnT 1/2, nVidia GeForce 1/2/3/4/5/6 series, le 3Dfx Voodoo Banshee, le Matrox Mystique/Millenium, Intel i810/815, SiS 300/315/330, Trident Cyberblade, VIA Unichrome). Come per gli altri software visti prima, anche questo permette l'utilizzo di un telecomando ad infrarossi per il controllo delle funzionalità.

In ogni caso, su http://www.lirc.org/receivers.html potete trovare qualche spunto per costruire un telecomando ad infrarossi sfruttando la porta seriale del PC.

## Freevo

Ispirato al servizio TiVo, troviamo Freevo (http://freevo.sourceforge.net/), interessante perché funziona già a partire da sistemi con CPU a 400MHz e si basa su librerie scritte con il linguaggio Python, abbastanza diffuso nel mondo open source non solo nell'ambito dell'elettronica o delle applicazioni multimediali.

Certo sono concetti "innovativi" ed "avveniristici" per un certo tipo di legislatore italico, me ne rendo conto, ma nel pieno rispetto delle leggi che tutelano i contenuti d'autore, è pur sempre una forma di fruizione, per altro penso permetterebbe un versamento diretto delle royalties a chi "produce" l'opera e/o ne detiene i diritti, senza "intermediazioni" di sorta.

## Riferimenti

- http://www.mythtv.org/
- http://www.dreamux.it/
- http://www.geexbox.org/
- http://freevo.sourceforge.net/
- http://www.lirc.org/receivers.html
