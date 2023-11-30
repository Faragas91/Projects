# Eingabe: RNA-Sequenz (String, der nur aus C, G, A und U besteht)

# Ausgabe: ORF (inkl. Start- und Stoppcodon) pro Zeile

# Als Start-Codon wird AUG verwendet, als Stopp-Codon sind UAG, UGA und UAA möglich.

# Hinweis: Zur Vereinfachung können Sie davon ausgehen, dass es keine Überlappungen gibt und dass das Start-Codon nicht innerhalb des ORF erneut vorkommt.
# Es muss auch nicht geprüft werden, ob innerhalb des ORF nur Basen-Triplets vorkommen.

rna = "CUCAUGCAUACAGUGUAAGCAGGAAGUAUGUAUUUUGUAUAGGCC"
new_rna = []
start_codon = "AUG"
stop_codon = ["UAG", "UGA", "UAA"]

for i in range(0, len(rna)):
    codon = rna[i:i+3]      
    if codon == start_codon:
        sub_len = rna.split(codon)
        break

for j in range(1, len(sub_len)):
    new_rna.append(start_codon + sub_len[j]) 

orf_list = []  # Liste, um alle ORFs zu speichern

for u in range(0, len(new_rna)):
    bla = ""  # Setzen Sie den Inhalt von bla zurück
    bla += new_rna[u]
    for k in range(0, len(bla)):
        codons = bla[k:k+3]
        if codons in stop_codon:
            orf = bla.split(codons, 1)[0] + codons
            orf_list.append(orf)  # Hinzufügen des ORF zum Ergebnis
            break

print(sub_len)
print(new_rna)  
print(orf_list)