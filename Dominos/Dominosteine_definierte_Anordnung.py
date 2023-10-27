with open("Dominos/domino_steine_4.txt", "r") as file:
    inhalt = file.readlines()
    inhalt = [zeile.strip() for zeile in inhalt]

aktuelle_kette = [inhalt[0]]
inhalt = inhalt[1:4]

i = 0
while i < len(aktuelle_kette):
    j = 0
    new_inhalt = []
    while j < len(inhalt):
        if aktuelle_kette[i][2] == inhalt[j][0]:
            aktuelle_kette.append(inhalt[j])
        elif aktuelle_kette[i][2] == inhalt[j][2]:
            inhalt[j] = inhalt[j][2] + " " + inhalt[j][0]
            aktuelle_kette.append(inhalt[j])
        else:
            new_inhalt.append(inhalt[j])
        j += 1
    inhalt = new_inhalt
    i += 1

print(aktuelle_kette)




        


'''
if inhalt[0][2] != inhalt[1][0]:
    inhalt[1] = inhalt[1][2] + " " + inhalt[1][0]
    '''
