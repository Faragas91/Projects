# Erstellen Sie ein Programm, das eine beliebige Aminosäurenkette in eine DNA-Sequenz übersetzt.

# Das Programm wird mit zwei Kommandozeilen-Argumenten gestartet:
# 1. Argument ist der Dateipfad zur DNA-Aminosäuren-Mapping-Datei
# 2. Argument ist die zu übersetzende Aminosäurenkette

# Das Programm liest die Aminosäurenkette ein und erzeugt die passende DNA-Sequenz.

# Buchstaben, die zu keinem Protein passen, sollen übersprungen werden.

# Die Eingabe-Sequenz liegt in Großschreibung vor.

# Für die Ausgabedatei können Sie Groß- oder Kleinschreibung beliebig wählen.

# Verwenden Sie die auf Moodle hinterlegte Mapping-Datei uebung3_map.txt – Diese enthält zwei Spalten: Codon und Aminosäure (getrennt durch ein Leerzeichen) Nachdem mehrere Codons für eine Aminosäure stehen können, können Sie aus den passenden Aminosäuren eine beliebige wählen (z.B. die erste in der Liste).

# Hinweis: Auf biologische Korrektheit muss nicht geprüft werden.

import random

with open("Translate_Protein_DNA_and_DNA_Protein/uebung3_map.txt", "r") as file:
    inhalt = file.readlines()
    inhalt = [zeile.strip() for zeile in inhalt] 

amino = "MTSGAHCNL "
stop_codon = ["TAG", "TGA", "TAA"]
seq = ""

while True:
    for j in amino:
        for i in inhalt:
            if j == i[4]:
                seq += i[:3]
                break
        if j == " ":
            seq += random.choice(stop_codon)
    break

print(seq)