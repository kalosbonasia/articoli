# Sistema operativo Linux – 1. Introduzione

**Autore:** Calogero Bonasia  
**Pubblicazione:** Elettronica Flash – linuxteam, marzo 2004  
**Licenza:** [CC BY-ND 4.0](https://creativecommons.org/licenses/by-nd/4.0/)

---

Perché proprio Linux? Perché, oltre ad avere un ampio supporto di applicativi, come vedremo più avanti, è un vero Sistema Operativo, è *preemptive*, offre un pieno multitasking, è robusto, affidabile, efficiente, flessibile, versatile.

Perché è uno UNIX a tutti gli effetti, migliore di altri su certe cose, più giovane su altre, è la via più logica per imparare e usare UNIX sul computer di casa. Perché è gratuito, perché è Open Source (vedremo che cosa significa). Perché, come ogni Sistema Operativo UNIX, è scarsamente vulnerabile al concetto di virus, quindi è piuttosto difficile che qualcuno spenda tempo a scriverne uno per Linux, sapendo che tanto non servirà a molto. Perché Linux cambia radicalmente (in positivo) il modo di vedere il computer e l'informatica, vi impedisce di annoiarvi, vi fa crescere culturalmente, può darvi molte soddisfazioni e insegnarvi concetti utili nel mondo del lavoro. Perché Linux è stato portato su un numero notevole di piattaforme, comprese le workstation più blasonate, come le Digital Alpha e le SUN Sparc e, quindi, spendere tempo per "giocarci" può servire ad imparare qualcosa che potrete utilizzare anche "da grandi". Linux is fun… enjoy Linux!

## Da dove cominciare?

La prima raccomandazione che posso farvi, quindi, è quella di leggere l'abbondante materiale riguardo Linux a disposizione su Internet. Prima di partire con l'installazione di Linux, spendete un po' di tempo per familiarizzare con la terminologia e la sintassi dei comandi. Vi accorgerete che installare un secondo sistema operativo sul vostro computer è solo un pochino più complesso che installare una suite di programmi per ufficio. Potete ricorrere anche ad una "live distro", cioè ad una installazione completa e perfettamente funzionante di Linux ma su CD-ROM, di modo che non compromettiate il vostro attuale sistema operativo, se proprio non siete sicuri di cosa volete fare o che Linux vi possa appassionare, e magari passare ad una vera e propria installazione in un secondo momento. A mio parere una buona introduzione a Linux è quella prodotta da Marco Pratesi, si trova sul sito http://www.telug.it/marco/LinuxIntro/LinuxIntro/node1.html. Esistono anche degli ottimi testi, suggerisco di orientarsi su quelli della casa editrice Apogeo (www.apogeonline.com) o Mc Graw Hill (www.mcgraw-hill.it), che da sempre offrono ottime traduzioni di testi in lingua inglese, per chi non ha difficoltà con la lingua inglese, invece, i libri di O'Reilly sono un must (www.ora.com).

## Cos'è una distribuzione?

Utilizzare Linux sarebbe ben più complesso se si avesse a disposizione solo il codice sorgente del kernel, dei vari tools e degli applicativi: è più comodo avere un CD con kernel e applicativi già compilati e un buon programma di installazione. La licenza che inizialmente Linus Torvalds (il creatore di Linux) scelse avrebbe ostacolato la nascita delle distribuzioni più diffuse, come la RedHat, dato che impediva a chiunque di conseguire un guadagno da Linux. Successivamente, Linus si convinse a scegliere la licenza GNU: oggi RedHat può chiedervi denaro per la produzione dei CD e per il supporto tecnico, lasciandovi liberi di utilizzare gratuitamente Linux grazie ai CD in omaggio sulle riviste o a quelli più o meno "artigianali", masterizzati dopo pazienti download probabilmente disponibili presso il Linux User Group della vostra città.

Le varie distribuzioni differiscono per il "target", per l'organizzazione del file system e dei file di partenza e di configurazione, per la quantità e l'aggiornamento del materiale offerto, per il tipo di pacchettizzazione, eccetera. Per esempio, da certi punti di vista, Linux Slackware differisce da Linux RedHat più di quanto possano differire tra loro due distinti Sistemi Operativi UNIX di tipo commerciale. D'altro canto, dal punto di vista dell'utente che non deve fare amministrazione di sistema, l'una distribuzione o l'altra fa poca differenza: può percepire più che altro la quantità e l'aggiornamento degli applicativi installati.

Ognuno ha il suo personalissimo punto di vista sulle distribuzioni Linux. Storicamente, Slackware è la prima distribuzione abbastanza completa e facile da usare; fino a qualche anno fa era senz'altro la più diffusa. Attualmente non è tra le più semplici, è un po' "per smanettoni", non è molto abbondante, ha un supporto limitato, per certi versi è obsoleta (esempio: assenza di dipendenze tra i pacchetti, difficoltà nell'aggiornamento). Comunque ha ancora un suo "mercato", può avere un interesse didattico e per molti versi è bella e affascinante.

Attualmente, la più diffusa è probabilmente la RedHat, in buona misura grazie al numero di sviluppatori impiegati, alla validità del suo metodo di pacchettizzazione (RPM = Redhat Package Manager), al supporto commerciale, alla facilità d'installazione, configurazione (autoprobing) e uso. La Debian estremizza l'aspetto free, offrendo il Linux GNU per eccellenza, senza un'azienda dietro e con sviluppatori disseminati per il mondo. È probabilmente la più completa e rigorosa ed è piuttosto complessa per l'amministratore di sistema.

La Mandrake somiglia molto alla RedHat, di cui utilizza la maggior parte dei pacchetti. La consiglio a chi non ha alcuna dimestichezza con Linux, soprattutto per la capacità del programma di installazione di configurare in maniera abbastanza semplice, una buona quantità di periferiche presenti sul vostro calcolatore. Permettetemi quindi di dare il trofeo di migliore distribuzione, a mio personale avviso, alla distribuzione tedesca, la SuSE. Abbondante di software, molto orientata alla comodità del desktop e all'uso "personal", da sempre ha avuto un occhio di riguardo proprio per i radioamatori, offrendo una buona selezione di programmi pronti all'uso.

## Il protocollo TCP/IP e AX.25, cose utili da sapere

Linux supporta pienamente i protocolli TCP/IP, non a caso numerosi servizi per radioamatori su Internet sono ospitati su server Linux. Per approfondire l'argomento vi suggerisco di leggere i seguenti documenti, disponibili sul sito ufficiale della documentazione Linux www.linuxdoc.org oppure sul sito del PLUTO, www.pluto.linux.it, dove potrete trovarvi anche molti documenti tradotti in lingua italiana:

- Network Administrator's Guide
- Linux Networking Howto
- AX25 Howto

È disponibile un vasto numero di applicativi per Linux specifici per i radioamatori, un sito dove è possibile trovare un nutrito elenco è http://radio.linux.org.au/. Altri pacchetti sono altrimenti reperibili su http://www.ibiblio.org/pub/Linux/apps/ham/. Un sito che raccoglie numerose applicazioni per il mondo Linux e open source in generale è www.freshmeat.net (vi consiglio anche di visitare www.sourceforge.net).

## Il filesystem

Nei sistemi DOS siamo abituati a riferirci alle varie unità disponibili utilizzando le lettere dell'alfabeto, quindi A: sarà il primo dischetto, C: il primo disco fisso, G: l'area locale della rete. In un sistema Linux o più in generale Unix l'utente non deve avere conoscenza delle caratteristiche della macchina, in quanto la gestione della macchina è riservata all'amministratore del sistema. All'utente viene presentato un unico dispositivo, come fosse un unico disco. In realtà alcune sottodirectory di questo dispositivo sono gli altri dispositivi fisici.

Le principali directory standard di ogni sistema Linux sono: `/bin` (programmi principali del sistema), `/dev` (file speciali per i dispositivi), `/etc` (file di configurazione del sistema), `/home` (aree private degli utenti), `/lib` (librerie di sistema), `/mnt` (directory per montare dispositivi), `/proc` (filesystem virtuale con informazioni sul sistema), `/root` (directory privata dell'amministratore), `/sbin` (programmi di amministrazione), `/tmp` (file temporanei), `/usr` (la maggior parte dei programmi installati), `/var` (log e file di sistema modificati).

Ci occuperemo di software per satelliti, automazione dello shack, packet radio, codice morse, AMTOR e PACTOR, SSTV e Faxsimile, software per la progettazione e l'autocostruzione, software di tipo educativo e di apprendimento delle basi dell'elettronica e della radiotecnica, e curiosità, come ad esempio i ricevitori software basati su Linux o sistemi per l'analisi dei segnali.
