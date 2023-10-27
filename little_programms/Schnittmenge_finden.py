# Erstellen Sie ein Programm, das Wörter aus zwei Dateien einliest und jene Wörter ausgibt, die in beiden Dateien vorkommen.
# Sie können die Dateipfade entweder vom Benutzer abfragen, oder Sie verwenden fixe Dateinamen (diese müssen dann input1.txt und input2.txt lauten!).
# Absolute Dateisystem-Pfade sind nicht erlaubt! Verwenden Sie nur relative Pfadangaben.
# Hinweis: Sie können davon ausgehen, dass die Wörter in Kleinbuchstaben und ohne Satzzeichen in den Dateien stehen. 
# Die Wörter sind durch Leerzeichen oder Zeilenumbrüche voneinander getrennt.


with open("little_programms/input1.txt", "r") as file:
    inhalt1 = file.read()

with open("little_programms/input2.txt", "r") as file:
    inhalt2 = file.read()

# Text in Wörter aufteilen und in eine Liste packen
woerter_liste1 = inhalt1.lower().split()
woerter_liste2 = inhalt2.lower().split()

rightWords = []

for i in woerter_liste1:
    for j in woerter_liste2:
        if i == j:
            rightWords.append(i)
        
print(rightWords)
