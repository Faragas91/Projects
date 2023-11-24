with open("Dominos/domino_steine_3.txt", "r") as file:
    inhalt = file.readlines()
    inhalt = [zeile.strip() for zeile in inhalt]

längste_kette = []
aktuelle_kette = [inhalt[0]]

i = 0
while i < len(inhalt):
    j = i + 1
    while j < len(inhalt):
        if aktuelle_kette[-1][2] == inhalt[j][0]:
            aktuelle_kette.append(inhalt[j])

        elif aktuelle_kette[-1][2] != inhalt[j][0]:
            if len(aktuelle_kette) > len(längste_kette):
                längste_kette = aktuelle_kette.copy()
            aktuelle_kette = []
            aktuelle_kette = [inhalt[j]]
            break
        j += 1
    i += 1

print("Längste Kette:", längste_kette)
print("Länge der Kette:", len(längste_kette))
