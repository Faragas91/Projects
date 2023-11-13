# Erstellen Sie ein Programm, das eine beliebige DNA-Kette in ein Protein übersetzt.

# Das Programm liest die DNA-Kette ein und erzeugt das passende Protein (Aminosäurenkette) aus den einzelnen Codons.

# Sollte die Länge der DNA-Kette nicht durch 3 teilbar sein, soll das Programm einen Fehler ausgeben und beenden.

# Sequenzen, die zu keinem Protein passen, sollen übersprungen werden (z.B. Stopp-Codons, oder Buchstaben, die kein Nukleotid darstellen)

# Die Eingabe-Sequenz liegt in Großbuchstaben vor.

# Für die Ausgabedatei können Sie Groß-/Kleinschreibung beliebig wählen.

# Verwenden Sie die auf Moodle hinterlegte Mapping-Datei uebung 3 _map.txt – Diese enthält zwei Spalten: Codon und Aminosäure (getrennt durch ein Leerzeichen)
# Hinweis: Auf biologische Korrektheit muss nicht geprüft werden (Start-/Stopp-Codons, etc.)

with open("Translate_Protein_DNA_and_DNA_Protein/uebung3_map.txt", "r") as file:
    inhalt = file.readlines()
    inhalt = [zeile.strip() for zeile in inhalt] 

seq = "cgttacgcttcctgagtggatgtacgtcgtttcgaacgcgagagtttggatagctgagagaggtac"
seq = seq.upper()
stop_codon = ["TAG", "TGA", "TAA"]
nukleotide = []

while True:
    if len(seq) % 3 != 0:
        print("Die Sequenz ist nicht durch 3 teilbar und wird abgebrochen")
        break
    else:
        print("Die Sequenz ist durch 3 teilbar und wird fortgesetzt")

    for i in range(0, len(seq), 3): 
        nukleotide.append(seq[i:i+3])

    protein = ""
    for k in nukleotide:
        for u in inhalt:
            if u[:3] == k:
                protein += u[4]
                break
        if k in stop_codon:
            protein += " "
    break

print(protein)