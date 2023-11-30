# – Leeres Array initialisieren (z.B. int numbers[15];)

# – Array mit Zufallszahlen (1-100) füllen

# – Bubble Sort

#     ● Aufeinanderfolgende Elemente vertauschen, wenn diese in der falschen Reihenfolge sind
#     ● Wiederholen, solange ein Tausch stattgefunden hat

from random import randint

bubble = []

for _ in range(15):
    bubble.append(randint(1, 100))

print("Vorher:  " + str(bubble))

for i in range(len(bubble)):
    for j in range(i + 1, len(bubble)): 
        if bubble[i] > bubble[j]:
            bubble[i], bubble[j] = bubble[j], bubble[i]

print("Nachher: " + str(bubble))