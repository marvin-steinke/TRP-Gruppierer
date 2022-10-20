# Gruppierer für die Turnierreifeprüfung des Deutschen Fechterbunds

TRP Gruppierer ist ein simples python GUI Tool zur Eingruppierung von
Prüflingen der Turnierreifeprüfung des Deutschen Fechterbunds. Bei Vorgabe der
Anzahl an Prüfenden wird eine Gruppierung vorgeschlagen und eine manuelle
Veränderung via Drag and Drop ermöglicht. Gruppen werden anschließend in die
PDF Beobachtungsbögen eingefügt und abgespeichert.

## Nutzung

Schaltflächen:

CSV-Datei: TRP Gruppierer verwendet als Datenquelle die Teilnehmerliste aus
ophardt.online im CSV Dateiformat. Über die Schaltfläche kann diese aus dem
Dateisystem ausgewählt werden. Andere Formate werden nicht unterstützt.

Beobachtungsbögen erstellen: Unter optionaler Angabe von Ort und Datum der TRP
werden die Gruppen von Prüflingen in die Beobachtungsbögen eingefügt und an
gewünschter Stelle im Dateisystem abgespeichert.

Gruppenanzahl +-: Mithilfe dieser Schaltfläche kann die Gruppengröße verändert
werden. Für die Umsetzung ist die folgende Schaltfläche notwendig.

Neu gruppieren: Die Prüflinge werden nach aktueller Gruppenanzahl neu
eingruppiert.

<br>

Mithilfe von Drap and Drop können Prüflinge zwischen Gruppen manuell verschoben
werden. Zur Übersicht des Gruppierungsprozesses werden die Prüflinge im
Programm in der Form 
<br>
`
'<Alter><Geschlecht>, <Verein>, <Nachname> (<geprüfte Waffe>)'
`
<br>
abgebildet; im Beobachtungsbogen hingegen, in der Form 
<br>
`
'<Vorname> <Nachname>, <Verein>, <Alter> J.'
`.
