# Sistema operativo Linux – seconda parte

**Autore:** Calogero Bonasia  
**Pubblicazione:** Elettronica Flash – linuxteam, aprile 2004  
**Licenza:** [CC BY-ND 4.0](https://creativecommons.org/licenses/by-nd/4.0/)

---

In questo secondo appuntamento andremo quindi subito a dare un'occhiata ai programmi che troviamo "in dotazione" con la nostra distribuzione. Avviando la nostra linux box, verrà chiesto di autenticarsi, immettiamo quindi il nostro nome utente e la password. Successivamente, individuiamo il programma YaST, che è quel programma che aiuta l'utente a configurare il sistema ed anche quindi ad installare o rimuovere i programmi. Vi verrà chiesto di immettere la password di root, cioè di quell'utente che avremo già configurato al momento dell'installazione, che è autorizzato ad eseguire modifiche al sistema.

Dopo di che dovrete selezionare la voce "Installare/Togliere i pacchetti", con un solo clic del tasto sinistro del mouse. Si aprirà una finestra di applicazione che permette di vedere i programmi installati sul sistema e quelli installabili.

## Gestione dei pacchetti con YaST

Concentrando la nostra attenzione sulla parte in alto a sinistra, avremo un menu a discesa di opzioni che ci permettono di filtrare i pacchetti (si chiamano così in gergo i programmi), in base al tipo. L'opzione predefinita, di solito è "cerca", il che permette di inserire il nome completo o una parte di esso del pacchetto che ricerchiamo, immediatamente sotto, nell'area di immissione testo. Ad esempio, se vogliamo sapere se abbiamo installato le librerie GCC sul sistema, si scriverà "gcc" e si premerà il tasto "cerca".

È intuitivo: cliccando sul quadratino con il tasto sinistro del mouse, si seleziona l'opzione per l'installazione, evidenziata dal segno di spunta. Se si riclicca sul medesimo, apparirà un segno simile ad una "zeta" su campo verde (sono in realtà due frecce opposte): esso significa che verrà effettuato un aggiornamento automatico del sistema specifico per quel pacchetto. Agendo alla stessa maniera ma usando però i tasti "+" e "-" si ottiene l'effetto di selezionare una installazione, rispettivamente, o di rimuovere il pacchetto (il simbolo è un bidone dell'immondizia).

Sulla parte in basso a destra della schermata, noteremo la funzione "Controlla le dipendenze" e accanto ad essa una checkbox che ci permette di avviare in automatico un controllo sulle dipendenze di quel pacchetto. Brevemente, una dipendenza sta ad indicare se quel pacchetto che intendiamo installare o rimuovere è legato ad altri pacchetti, e la cui mancanza potrebbe causare il malfunzionamento della macchina.

## Programmi per radioamatori

Altro metodo per consultare i pacchetti installati sul sistema è quello per categorie. Nel combo box in alto a sinistra del programma YaST, potremo scegliere la funzione "Gruppi di pacchetti". Scorrendo l'elenco per tipologia, nella parte sinistra dello schermo, individuiamo la voce "Produttività" e poi la voce "Radioamatori".

I pacchetti specifici per i radioamatori, in dotazione alla distribuzione SuSE Linux sono suddivisi per: Fax (trasmissione immagini in facsimile), Satellite (programmi di tracking), psk31 (di significato omonimo), packet e morse (di evidente riferimento), Registrazione log (programmi di log di stazione) e infine la voce "Altro" che raccoglie programmi non afferenti alle categorie precedenti, come quelli per trasmissione SSTV oppure un programma per APRS o ancora il programmino per controllare l'ICOM PCR-1000.

Come detto, installare un programma è abbastanza semplice, basta cliccare sul suo quadratino di riferimento fintanto che si evidenzia il segno di spunta e proseguire con il bottone "Accetto". Verrà eventualmente chiesto di inserire il CD o DVD opportuno e attendere la ricompilazione delle dipendenze al livello di sistema.

I programmi per radioamatori vanno a finire nel menù apposito, ma non sempre. Infatti alcuni programmi non seguono lo standard di generazione automatica del menù, e vanno individuati a mano sul sistema. Si procede quindi aprendo una finestra di terminale. Di solito i programmi eseguibili, sono collocati sotto il percorso `/usr/bin`; è sufficiente quindi richiamarli con la sintassi `./nomeprogramma` per lanciarli. Attenzione: il punto e la barra sono importanti, dicono appunto di lanciare quell'apposito programma.

## Esempio: HamLog e XLOG

Nel mio esempio, lancio il programma HamLog (scritto da uno studente: Nuno Sucena Almeida, come vi avviserà lo stesso ad ogni suo avvio), precedentemente scelto dal gruppo di programmi per radioamatori mediante YaST. Aprendo quindi una shell, digitiamo:

```
cd /usr/bin
./hamlog
```

Si aprirà la finestra del programma, di uso abbastanza semplice e per questo anche molto limitato nelle sue funzionalità, ma quello che è importante in questo senso è trasmettere i principi per lanciare un programma.

Esistono altri programmi di logging, migliori di HamLog, come ad esempio l'ottimo XLOG, che è reperibile all'indirizzo http://www.qsl.net/pg4i/download/. La pagina principale, per avere informazioni sul progetto è invece http://www.qsl.net/pg4i/. In questo sito troverete anche altri programmi specifici per il nostro mondo, alcuni di questi li vedremo in dettaglio più avanti.
