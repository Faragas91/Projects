from collections import Counter

# Datei öffnen
with open("little_programms/input1.txt", "r") as file:
    inhalt = file.read()

# Inhalt wird durch Sonderzeichen und Leerzeichen getrennt
word_list = inhalt.split()
clean_word_liste = [word.strip(".,!?") for word in word_list]
print(clean_word_liste)

number_list = []

# Schleife die die Länge jedes Wort in eine leere Liste hineinschreibt
for word in clean_word_liste:
    number_list.append(len(word))

print(number_list)

# Counter zählt wie oft eine Zahl herauskommt
number_frequency = Counter(number_list)

# Ausgabe der Häufigkeit der Zahl
for number, frequency in number_frequency.items():
    print(f"Zahl {number} kommt {frequency} Mal vor.")

        
