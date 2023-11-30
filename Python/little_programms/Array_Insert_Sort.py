# – Leeres Array initialisieren (z.B. int numbers[15];)

# – Array mit Zufallszahlen (1-100) füllen

# – Insertion Sort

#     ● Suche kleinstes Element und gib es an die erste Stelle in einem zweiten Array
#     ● Wiederholen, aber eingefügte Elemente nicht erneut einfügen

    
# – Array vor und nach Sortierung ausgeben

from random import randint

liste = []
insert = []
for _ in range(15):
    liste.append(randint(1, 100))

print("Vorher:  " + str(liste))

while range(len(liste)):
    min_Wert = min(liste)
    liste.remove(min_Wert)
    insert.append(min_Wert)

print("Nachher: " + str(insert))
