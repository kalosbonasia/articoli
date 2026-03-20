# Sistema operativo Linux – Installazione SuSE

**Autore:** Calogero Bonasia  
**Pubblicazione:** Elettronica Flash – linuxteam, aprile 2004 (inserto)  
**Licenza:** [CC BY-ND 4.0](https://creativecommons.org/licenses/by-nd/4.0/)

---

Accendete il computer e tutto l'hardware ad esso connesso. Inserite il CD numero 1 o il DVD nel lettore.

Nella schermata di partenza potete scegliere un modo di installazione o caricare un sistema già installato. Alla fine dell'installazione, il CD può essere usato per installare altro software. Il caricamento di un sistema preinstallato è evidenziato, perché è l'opzione più frequentemente selezionata. Tuttavia, se sul vostro sistema dovesse essere già presente una installazione di Windows o un altro sistema operativo, noterete come prima opzione "Boot from Hard Disk". Dovete quindi premere i tasti-freccia e selezionare "Installation". Se premete il tasto F2 potrete selezionare una risoluzione dello schermo, tra quelle supportate dalla vostra scheda video; se avete dubbi, scegliere una 640x480 oppure scegliere la modalità solo testo. Questa selezione riguarda solo il programma di installazione.

Selezionate subito dopo la lingua di installazione (che rimarrà anche come scelta di lingua predefinita) e vi troverete alla schermata di scelta dei pacchetti software e di partizionamento del disco fisso predeterminata. Nel caso vi fosse già una installazione Windows, essa verrà rilevata ed automaticamente impostata come partizione montabile da Linux (in lettura e scrittura se essa è formattata in FAT32, in sola lettura se è formattata come NTFS).

Nel mio esempio si parte dalla considerazione che abbiate dello spazio libero sul vostro hard disk sul quale si andrà ad installare Linux. Nel caso non ve ne fosse, SuSE Linux in versione 9.0 permette di partizionare in maniera abbastanza intuitiva il disco, ricavando uno spazio libero adeguato e gestendo le opportune impostazioni per Windows. Un po' come fa il noto programma di partizionamento Partition Magic. In questo caso tenete presente che la funzione appena detta lavora sulla base dei settori liberi del disco, vi consiglio quindi di procedere ad una preliminare deframmentazione del disco, da Windows, in modo da riservare quanto più possibile spazio libero alla "fine del disco".

Piccola disquisizione tecnica: se il vostro sistema ha un file di swap permanente su un file system NTFS (di solito quello adottato da Windows NT, 2000 o XP), questo file potrebbe trovarsi alla fine del disco rigido e restarci anche dopo una deframmentazione. Di conseguenza, potrebbe rivelarsi difficile ridurre la partizione alle giuste dimensioni e fare spazio per Linux. In questo caso, riavviate il sistema con Windows, disattivate temporaneamente il file di swap (la memoria virtuale) di Windows e procedete all'installazione di Linux. Dopo l'installazione, potrete riconfigurare di nuovo tutta la memoria virtuale.

## Partizionamento

Per la maggior parte degli utilizzi "domestici", bastano due partizioni, una di root ("/") e una di swap, pari al doppio della memoria RAM disponibile. Permane il consiglio di leggere prima il manuale fornito con la confezione di SuSE Linux, oppure gli "appunti di informatica libera" di Daniele Giacomini, reperibili su http://a2.swlibero.org/, in particolare alla sezione numero quattro: "installare GNU/Linux".

L'installazione procederà con la copia dei pacchetti dai CD al disco fisso, chiedendo di volta in volta, quando necessario, di inserire il CD specifico. Al termine, la macchina si avvierà automaticamente per riproporre le schermate di configurazione delle periferiche individuate dalla procedura di installazione, ad esempio la scheda di rete, le altre periferiche di comunicazione come il modem, e così via. Per ciascuna periferica è bastevole cliccare sulla voce apposita e seguire le chiare istruzioni della YaST stessa. Se non siete sicuri di quello che state facendo, preferibilmente lasciate i parametri preimpostati proposti dall'installazione.

Una peculiarità della SuSE Linux è quella di ricercare in automatico gli ultimi aggiornamenti relativi alla distribuzione, se viene rilevata una connessione ad Internet valida. Se utilizzate ADSL, è consigliato procedere all'aggiornamento. Altrimenti, siccome la procedura potrebbe durare parecchi minuti e scaricare anche molti megabyte di dati, è preferibile rinviare ad un secondo momento.

## Configurazione finale

Al termine dell'installazione vi mancheranno ancora tre parametri importanti: per prima cosa dovete specificare una password per l'amministratore del sistema (l'utente root). Fate attenzione a non dimenticare la password di root, dal momento che è l'unica che vi permette di modificare il sistema o di installare programmi.

Successivamente viene chiesto di specificare in che contesto di rete lavorerà il vostro computer, se cioè lo utilizzerete in maniera indipendente da un Name Service o meno. Di solito, per l'uso domestico, si sceglie l'opzione "Stand Alone Machine" e subito dopo si crea l'utente locale, quello che utilizzerete comunemente per le normali attività di lavoro (ricordate che root si dovrebbe usare solo per le attività di amministrazione, come installazione di programmi).

Infine viene fornita una lista di altri componenti del sistema rilevati, tra cui la scheda grafica. Se necessario, modificate i valori di risoluzione grafica o di profondità cromatica dello schermo. Fate attenzione a non mettere valori a caso: se non sapete cosa impostare rischiate di danneggiare seriamente il monitor.

## Come Linux identifica i dispositivi

Linux non assegna una lettera ad ogni periferica di memorizzazione di massa, a differenza di Windows. Linux identifica i dischi fissi distinguendoli per tipologia di funzionamento: un disco di tipo IDE sarà identificato dalla sigla "hd" e dalla prima lettera dell'alfabeto (`hda` rappresenta il primo disco fisso sul primo canale IDE, `hdb` il secondo, e così via). Per i dischi con tecnologia SCSI il discorso è similare (`sda` rappresenta il primo disco fisso SCSI rilevato).

Ogni disco fisso potrà contenere una o più partizioni, ogni partizione viene contrassegnata da un numero: `hda1` rappresenta la prima partizione sul primo disco fisso IDE. Le partizioni estese partono dalla numerazione 5 in avanti.

Per lavorare su un disco è necessario "montarlo", cioè renderlo fruibile al sistema. I comandi che spiegano al sistema operativo quali "dischi" montare in automatico sono contenuti nel file `/etc/fstab`. Per estrarre un CD o un floppy dal sistema, è necessario "smontarli" dal file system con il comando `umount /media/cdrom` (o `/media/floppy`). Digitando il comando `eject`, a CD smontato, si aprirà automaticamente il cassettino del lettore.
