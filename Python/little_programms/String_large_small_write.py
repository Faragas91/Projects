Text = "dAS ist EIn TesT"
Text = Text.lower()
outText = ""
n_Text = True

for i in range(len(Text)):
    if n_Text:
        outText += Text[i].upper()
        n_Text = False
        
    else:
        outText += Text[i].lower()

    if Text[i].isspace():
        n_Text = True

print(outText)