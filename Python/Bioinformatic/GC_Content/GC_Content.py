with open("Bioinformatic/GC_Content/gc_gehalt.txt", "r") as file:
    inhalt = file.readlines()
    inhalt = [zeile.strip() for zeile in inhalt] 

g_base = 0
c_base = 0
länge_seq = 0
seq = ""

for sequence in inhalt:
    for base in sequence:
        länge_seq += 1
        if base == "c":
            c_base += 1
        if base == "g":
            g_base += 1
            
    if len(sequence) == länge_seq:
        gc_base = g_base + c_base
        gc_gehalt = round((gc_base/len(sequence)) * 100, 0)
        seq += sequence
        print(str(gc_gehalt) + " " + sequence, "\n")
        länge_seq = 0
        g_base = 0
        c_base = 0
        
        









