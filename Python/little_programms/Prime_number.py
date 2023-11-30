versuche = 3
i = 2
teiler = []

while versuche > 0:
    try:
        eingabe = int(input("Geben Sie hier Ihre Zahl ein: "))
        break 

    except ValueError:
        print("Ihre Eingabe muss eine Zahl sein")
        versuche -= 1
        print("Sie haben noch " + str(versuche) + " Versuche")
        if versuche == 0:
            break
        


try:
    while i <= eingabe:
        if eingabe % i == 0:
            teiler.append(i)
            i += 1
        if eingabe % i != 0:
            i += 1

    if len(teiler) == 1:
        print(str(eingabe) + " ist eine Primzahl")
    else:
        print(str(eingabe) + " ist keine Primzahl")
        teiler.remove(eingabe)

                    
    print("Die Teiler sind: " + str(teiler))

except NameError:
    print("Die Eingabe " + str(eingabe) + "ist keine Zahl")