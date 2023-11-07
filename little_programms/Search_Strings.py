# – Eingabe:

# ● Zu durchsuchender String

# ● Suchwort/Pattern

# – Ausgabe:

# ● Positionen des Patterns im zu durchsuchenden String

# ● Anzahl der Vorkommen


# – Beispiel 1

# ● String: „Ich bin ein ich bin ein“, Pattern: „bin“

# ● Ausgabe: 4, 16. Anzahl: 2


# – Beispiel 2

# ● String: „wwww“, Pattern: „ww“

# ● Ausgabe: 0, 1, 2. Anzahl: 3


# – Beispiel 3

# ● String: „abc“, Pattern: „x“

# ● Ausgabe: Nicht gefunden

def stringSearch(string, pattern):
    liste = []

    try:
        for i in range(len(string)):
            ausgabe = string.find(pattern, i)
            if ausgabe != -1:
                liste.append(ausgabe)
                index = list(set(liste))
                index.sort()
        return index, len(index)

    except UnboundLocalError:
        print("Nicht gefunden")


print(stringSearch("Ich bin ein ich bin ein", "bin ein"))
print(stringSearch("wwww", "ww"))
print(stringSearch("abc", "x"))