# Sistema operativo Linux – terza parte: Gnome Predict

**Autore:** Calogero Bonasia  
**Pubblicazione:** Elettronica Flash – linuxteam, maggio 2004  
**Licenza:** [CC BY-ND 4.0](https://creativecommons.org/licenses/by-nd/4.0/)

---

Gnome Predict è un programma per il tracciamento del moto dei satelliti per l'ambiente desktop Gnome.

Il programma nasce come interfaccia del **Predict** di John A. Magliacane, KD2BD. Verificate sul sito web www.qsl.net/kd2bd dove troverete anche una buona quantità di informazioni relativamente all'attività satellitare. La licenza d'uso di Gnome Predict è la GNU General Public License che fondamentalmente consente di distribuire assieme al software anche i suoi sorgenti, modificabili liberamente, ma senza alcuna garanzia da parte dell'autore. C'è però il vantaggio che se si è in grado di farlo, si può intervenire direttamente sul codice stesso e quindi adattarlo alle proprie necessità.

La versione corrente di Gnome Predict permette l'inseguimento (tracking) di un gran numero di satelliti, visualizzando i parametri orbitali dei medesimi in un'apposita finestra. È possibile tenere aperte numerose finestre e mappe di tracciamento dei satelliti, sia separatamente, che raggruppate in una sorta di "notebook". Le liste possono essere organizzate alfabeticamente oppure stampate.

## Installazione

Dal sito http://groundstation.sourceforge.net/gpredict/ è possibile scaricare il programma. Selezionate i package già precompilati per la piattaforma di Linux da voi utilizzata. Ad esempio se utilizzate RedHat o Fedora, potreste scegliere la versione `gpredict-0.4.0-1_hamlib.rh8.i386.rpm` oppure la sua equivalente "sorgente", cioè da ricompilare sulla vostra macchina, contraddistinta dall'estensione `.src`. In linea di massima individuate quelle versioni che riportano "**i386**": sono le generiche relative al processore di tipo Intel, spesso vanno bene anche per processori AMD.

Per lanciare Gnome Predict occorre avere installato sulla propria linux box la versione 1.4 di Gnome o una superiore. Se utilizzate un altro desktop manager, per esempio KDE, dovrete installare le librerie di supporto per gli applicativi Gnome, le Gnomelibs inclusi i files "**header**", cioè i sorgenti di queste, per la ricompilazione, se necessaria.

Una volta scaricato il programma, l'installazione è semplice:

1. Aprite una finestra terminale
2. Divenite **root**
3. Posizionatevi nel percorso dove è collocato il file scaricato
4. Decomprimetelo con `tar zxvf nomedelfile`
5. Entrate nella cartella appena creata (di solito porta il nome del file senza le estensioni tar.gz)
6. Digitate `./configure`
7. Poi `make`
8. E infine `make install`

Per qualsiasi dubbio leggete il file INSTALL presente nella cartella dove vi siete posizionati.

## Utilizzo

Una volta lanciato **Gnome Predict**, dovrete impostare i parametri minimi relativi alla vostra posizione geografica, nel pannello apposito. È possibile tenere aperte numerose finestre e mappe di tracciamento dei satelliti.

Al momento in cui scrive, le specifiche dell'interfaccia hardware che permette di controllare i rotori d'antenna non sono ancora state rilasciate, ma sono in fase di ultimazione. Per il momento è possibile pilotare direttamente il proprio apparato ricetrasmettitore utilizzando un altro programma che si basa sulle specifiche di libreria comuni allo stesso Gnome Predict, **Gnome Rig**.

La base comune di librerie è la HamLib (http://hamlib.sourceforge.net/) per chi volesse approfondire. Gnome RIG permette di controllare l'accensione e lo spegnimento del vostro apparato, il livello dello AGC, selezionare filtri e ovviamente impostare la frequenza di funzionamento. Purtroppo non esiste un protocollo standard per il controllo degli apparati radioamatoriali predisposti, per cui sono state individuate delle specifiche per numerosi apparati, che potreste reperire sul sito delle HamLib, alla voce "Supported Radios". Un indicatore colorato accanto al nome dell'apparato vi indicherà se il programma funziona senza alcun problema (verde), se vi è ancora qualche imprecisione nel driver o se è in fase di sviluppo (arancione), oppure se il costruttore ha rifiutato di fornire le specifiche (rosso). In grigio vengono indicati quegli apparecchi che non hanno alcuna documentazione relativa alla porta di comunicazione con il PC.

## Riferimenti

- http://groundstation.sourceforge.net/gpredict/
- http://www.qsl.net/kd2bd
- http://hamlib.sourceforge.net/
