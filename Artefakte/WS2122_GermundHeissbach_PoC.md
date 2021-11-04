# PoC #1: Daten (Messwerte) der Sensoren mittels einer Systemschnittstelle abfragen/empfangen

### Beschreibung 
Als Systemschnittstelle könnte z.B. ein Raspberry Pi fungieren.  Die Sensoren sollen die gemessenen Werte (Temperatur und Wasserstand) an eine Schnittstelle senden können. Diese Schnittstelle soll Daten empfangen und abfragen können.

### Schritte 
* Die Sensoren sind in der Anlage installiert
* Die Sensoren messen die jeweiligen Messwerte (Temperatur, Wasserstand)
* Sie senden die gemessenen Daten an die Systemschnittstelle
* Die Schnittstelle empfängt die Daten und kann diese Weiterverarbeiten (Benachrichtigung von Nutzern, Speicherung, Auswertung, etc.)

### Exit Kriterien
Die Werte wurden erfolgreich gemessen, gesendet und empfangen. Eine Kommunikation zwischen den Systemen (Sensor  und Schnittstelle) ist möglich.
### Fail Kriterien
* Die Sensoren können keine Daten messen und senden
* Schnittstelle empfängt keine Daten
* Keine Verknüpfung der Systeme möglich

### Fallbacks
Sollten die Sensoren keine Werte messen können, sollten sie erneut kalibriert und evtl. neu installiert werden. Ist es nicht möglich eine Verknüpfung zwischen den Sensoren und der Schnittstelle herzustellen, soll mit Dummy Daten gearbeitet werden. Ggf. Hilft eine neue Installation und Konfigurierung der Schnittstelle.

# PoC #2: Erste Implementierungen und Installationen am Raspberry Pi

### Beschreibung 
Um den Raspberry Pi für das Projekt nutzen zu können muss dieser in mehreren Schritten für die Arbeit vorbereitet werden (Die Schritte orientieren sich nach folgendem Tutorial: https://tutorials-raspberrypi.de/automatisches-raspberry-pi-gewaechshaus-selber-bauen/).

### Schritte 
* Betriebssystem installieren
* Terminal öffnen
* Packages installieren und alles updaten
* benötigte Bibliotheken installieren (SpiDev, Adafruits)
* Raspberry Pi mit Strom versorgen (per GPIO oder USB Kabel)
* Spannung mittels Multimeter nachmessen
* Belegung der GPIOs, Programmierung der gewünschten Funktionen (Code ->Tutorials, Github)

### Exit Kriterien
Die beschrieben Schritte funktionieren und der Raspberry Pi ist für den weiteren Projekt Verlauf vorbereitet. Die Tests mit dem Multimeter und Jumper Kabel waren erfolgreich.

### Fail Kriterien
* Installationen nicht erfolgreich
* Spannungen nicht messbar
* Probleme bei der Stromversorgung (Im Worst Case kann eine zu hohe Spannung den Raspberry Pi beschädigen)
* Code funktioniert nicht

### Fallbacks
Zurücksetzen des Raspberry Pi‘s, dann eine erneute Durchführung der Schritte, ggf. andere Tutorials, Betriebssysteme und Bibliotheken nutzen und den Code anpassen. Genaue Fehleranalyse.
