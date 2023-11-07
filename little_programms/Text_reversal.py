# Eingabe: Text

# Ausgabe: Text, bei dem die einzelnen Worte verkehrt geschrieben sind. Hierbei soll jedes
# Wort mit einem Großbuchstaben beginnen und der Rest des Wortes klein geschrieben
# werden. Die Worte selbst bleiben jedoch in der richtigen Reihenfolge.

# Hci Nib Nie Iforp"


text = "Ich BIN EIN profi"
bla = ""

neu_text = text.split(" ")

for i in range(0, len(neu_text)):
    fusl = neu_text[i] [::-1] # gibt jedes einzelne Element aus der Liste zurück und dreht es um
    bla += fusl + " " # jedes Wort wird in bla eingelesen und eine Leerzeichen eingefügt

low_text = bla.lower()
outText = ""
n_Text = True

for i in range(len(low_text)):
    if n_Text:
        outText += low_text[i].upper()
        n_Text = False
        
    else:
        outText += low_text[i].lower()

    if low_text[i].isspace():
        n_Text = True

print(outText)
