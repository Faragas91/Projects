'''
Das Programm soll eine optimale Lösung für das Rückgeld eines bestimmten
Geldbetrages ermitteln

● User-Input: mögliche Münzen und Geldbetrag
Als Command-Line Arguments:
./wechsel 1234 100 50 20 2
Bedeutet: der Betrag 1234 soll mit den zur Verfügung stehenden Münzen mit
den Beträgen 100, 50, 20, 2 herausgegeben werden
Ergebnis: 12*100 + 1*20 + 7*2 = 1234

● Es können hier ganze Zahlen verwendet werden
(entspricht dann bspw. Cent-Beträgen)

● Ausgabe: Welche Münzen (in welcher Anzahl) müssen herausgegeben werden?
(Vereinfachung: die Münzen einzeln anzeigen. Statt 7*2 dann „2 2 2 2 2 2 2“)

● Optimal: möglichst geringe Anzahl an Münzen nötig

● Verwenden Sie dazu einen Greedy-Algorithmus
● → Wann liefert der Algorithmus schlechte Ergebnisse?
'''

hundertCent = 100
fuenfzigCent = 50
zwanzigCent = 20
zweiCent = 2

geld = 1234

# Hundert Cent
hundertDivision = geld // hundertCent
hundertRest = geld % hundertCent

# Fünfzig Cent
fuenfzigDivision = hundertRest // fuenfzigCent
fuenfzigRest = hundertRest % fuenfzigCent

# Zwanzig Cent
zwanzigDivision = fuenfzigRest // zwanzigCent
zwanzigRest = fuenfzigRest % zwanzigCent

# Zwei Cent
zweiDivision = zwanzigRest // zweiCent
zweiRest = zwanzigRest % zweiCent

result = (
    f"{hundertDivision}*{hundertCent} + "
    f"{fuenfzigDivision}*{fuenfzigCent} + "
    f"{zwanzigDivision}*{zwanzigCent} + "
    f"{zweiDivision}*{zweiCent}"
)

print(result)
