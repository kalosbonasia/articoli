# Costruire una rete wireless con Linux – settima parte: S.O. Linux

**Autore:** Calogero Bonasia  
**Pubblicazione:** Elettronica Flash – linuxteam, ottobre 2004  
**Licenza:** [CC BY-ND 4.0](https://creativecommons.org/licenses/by-nd/4.0/)

---

Come fare dialogare il vostro notebook e il vostro pc fisso senza l'ingombro dei fili.

Grazie alla sempre più crescente diffusione delle apparecchiature di trasmissione dati per computer senza fili, comunemente note come "wireless", si stanno diffondendo anche le periferiche adatte al sistema operativo Linux. Vediamo quindi come utilizzare una scheda di questo tipo per realizzare una piccola rete domestica, con funzioni di bridge, IP masquerading, routing, impiegando un notebook di provenienza surplus.

Il notebook l'ho reperito su http://annunci.tiscali.it, un ottimo sito di annunci, gratuito, senza beghe e perdite di tempo e di denaro tipiche di altri siti di aste on line o annunci a pagamento. Assicuratevi che il notebook abbia una porta di tipo PCMCIA II funzionante.

## Il kit Aviator 2.4

Da Webgear, uno dei principali costruttori di apparecchiature per trasmissione dati per computer, ho acquistato un kit "Aviator 2.4", un kit che comprende due schede PCMCIA tipo II e due ISA PCMCIA slot offerto per creare una LAN radio tra due notebook o due pc fissi o combinazioni di essi. La frequenza utilizzata da questi apparecchi è quella canonica di 2.4GHz, su standard IEEE 802.11 (frequency hopping e spread-spectrum), ovvero per 2Mbps di banda passante. Le schede vengono viste come normalissime schede Ethernet, sul nostro sistema Linux, quindi `eth0` ed `eth1`, quando saranno configurate. Sul kit viene indicata la compatibilità verso Linux, ma al suo interno vi sono solo i driver per i sistemi operativi Microsoft.

È necessario scaricare da Internet un modulo kernel caricabile denominato `ray_cs.o`, all'indirizzo http://www.webgear.com/support/software_top.html. L'autore del driver è Corey Thomas, che ha scritto il modulo sia per l'Aviator 2.4 Wireless kit che per i più costosi Aviator Pro e Raytheon Raylink. La versione da me utilizzata è la 1.68. Per installare il driver è sufficiente digitare:

```
cp ray_cs-1.68.tgz /usr/src/linux/pcmcia-cs-3.1.5
tar xvzf ray_cs-1.68.tgz
make config
make all
make install
```

## Configurazione della rete wireless

Per le prime prove ho creato una rete wireless paritetica, cioè il nodo A connetteva il nodo B. Prima di abilitare le schede è necessario editare il file `/etc/pcmcia/config.opts` e inserire la linea:

```
source ./ray_cs.opts
```

All'avvio il servizio di gestione delle schede PCMCIA leggerà il file `ray_cs.opts`. Questo file contiene alcuni settaggi importanti per fare funzionare la scheda Webgear:

```
module "ray_cs" opts "pc_debug=2 essid=LINUX hop_dwell=128 beacon_period=256 translate=1"
```

L'opzione `pc_debug=2` occorre perché il sistema si accorga dell'inserimento o disinserimento della scheda, leggendolo da `/var/log/messages`. Mentre `essid=LINUX` designa il nome della rete (nulla vieta di scrivere qualsiasi altro nome preferiate per la vostra rete wireless personale, purché non mettiate spazi o segni di interpunzione).

Il file da manipolare per la configurazione delle schede di rete è `/etc/sysconfig/network-scripts/ifcfg-eth0` e deve contenere:

```
DEVICE=eth0
IPADDR=192.168.0.100
NETMASK=255.255.255.0
NETWORK=192.168.0.0
BROADCAST=192.168.0.255
ONBOOT=yes
BOOTPROTO=none
USERCTL=no
```

Le schede devono essere avviate sequenzialmente. Di solito si sentono due beep consecutivi a conferma del corretto avvio. Cercate la stringa `ray_cs interrupt network "LINUX" started` nel log dei messaggi. Quando avvierete la seconda scheda, nel log troverete: `ray_cs interrupt network "LINUX" joined`, che sta ad indicare che le due schede si sono "viste" e stanno comunicando.

## Wireless masquerading e bridge

Poiché utilizzo una rete locale domestica ed alcuni apparecchi sono collocati in uno sgabuzzino per mancanza di spazio, ho deciso di utilizzare la connessione senza fili per connettere direttamente queste unità tra di loro e con il notebook che utilizzo in soggiorno per lavoro. Sfortunatamente le schede Aviator possono essere usate solo per connessioni punto a punto, a meno di non comperare un access point. Per una cifra inferiore ho comperato un altro pc usato, sempre sul solito sito, e grazie a Linux l'ho trasformato in un bridge.

Su questo server ho abilitato il routing del traffico wireless utilizzando il comando:

```
/sbin/route add 192.168.1.1 gw 191.168.0.
```

Per completare il lavoro ho attivato anche il masquerading sul protocollo IP:

```bash
#!/bin/sh
case "$1" in start)
/sbin/modprobe ip_masq_ftp
/sbin/ipchains -A forward -s 192.168.0.0/24 -j MASQ
/sbin/ipchains -A forward -s 192.168.1.0/24 -j MASQ
echo "NAT avviato" ;;
stop)
/sbin/ipchains -F
echo "NAT fermato" ;;
esac
```

Dopo avere abilitato una connessione PPP, lanciato le schede wireless e avviato il masquerading sul server, è stato possibile connettere il resto della rete ad Internet; l'importante è aggiungere la route giusta (`/sbin/route add default gw 192.168.1.1`).

In alternativa, potete utilizzare `brcfg` di Alan Cox (radioamatore ma anche famoso guru di Linux), come segue, per creare un bridge:

```
/sbin/ifconfig eth0 promisc up
/sbin/ifconfig eth1 promisc up
./brcfg -ena
```

Alla fine sarà possibile accedere qualsiasi computer della rete locale tramite il laptop di prova.

## Riferimenti

- http://annunci.tiscali.it
- http://www.dia.unisa.it/professori/masucci/sicurezza/firewall.pdf
- http://kidslink.bo.cnr.it/scuolan/libro/cap5-3-3.htm
- http://www.webgear.com
- http://www.ibiblio.org/pub/Linux/docs/HOWTO/Bridge
- http://www.tux.org/pub/net/alan-cox/
- http://www.linuxplanet.com/linuxplanet/tutorials/3086/1/
- http://www.wireless-italia.com/
- http://www.bertolinux.com/wireless/italiano/Wireless-HOWTO-6.html
- http://www.labcc.ch/linuxdoc/WirelessHOWTO.html
- http://www.linuxonline.it/print.php?sid=370
