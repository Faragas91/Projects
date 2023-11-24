hangman_drawings = [
    """
    _ _
    """,
    """
     |
    _|_
    """,
    """
     |
     |
     |
    _|_
    """,
      """
     |
     |
     |
     |
     |
    _|_
    """,
    """
     _______
     |     
     |
     |
     |
     |
    _|_
    """,
    """
     _______
     |     |
     |
     |
     |
     |
    _|_
    """,
    """
     _______
     |     |
     |     O
     |
     |
     |
    _|_
    """,
    """
     _______
     |     |
     |     O
     |     |
     |
     |
    _|_
    """,
    """
     _______
     |     |
     |     O
     |    /|
     |
     |
    _|_
    """,
    """
     _______
     |     |
     |     O
     |    /|\\
     |
     |
    _|_
    """,
    """
     _______
     |     |
     |     O
     |    /|\\
     |    /
     |
    _|_
    """,
    """
     _______
     |     |
     |     O
     |    /|\\
     |    / \\
     |
    _|_
    """
]

# Funktion für das Zeichnen des Hangmans
def draw_hangman(stage):
    print(hangman_drawings[stage])

"---------------------------------------------------------"

import random

while True:
    # Liste von verschiedenen Wörter
    word_list = ["apple", "banana", "orange", "grape", "watermelon", "hangman", "address", "control", 
                "feature","freedom", "imagine", "kitchen", "lantern", "mission", "natural", "pattern", 
                "quality", "release", "stations", "theater", "unusual", "vintage", "weather", "yellow",
                "zealous", "zombie",]        

    # Es wird eines aus den Wörtern zufällig ausgesucht
    random_word = random.choice(word_list)
    word = list(random_word) # Buchstaben der Wörter werden aufgesplittet
    result = ['_' for x in word]
    letters = []

    alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    special_characters = ['!', '@', '#', '$', '%', '&', '*', '(', ')', '-', '_', '+', '=', '{', '}', '[', ']', '|', ':', ';', ',', '.', '<', '>', '?']
    numbers = [str(i) for i in range(10)]

    difficulty = int(input("Wählen Sie Ihren Schwierigkeitsgrad aus: 1 für easy, 2 für normal, 3 für hard"))
    if difficulty == 1:
        draw_count = 0 # Zähler für den Hangman
        count = 12 # Zähler für die Versuche

    if difficulty == 2:
        draw_count = 4 # Zähler für den Hangman
        count = 8 # Zähler für die Versuche
    
    if difficulty == 3:
        draw_count = 8 # Zähler für den Hangman
        count = 4 # Zähler für die Versuche

    print("Die Länge des Wortes beträgt: " + str(len(word)))
    print("Sie dürfen " + str(count) + " mal falsch Antworten", "\n")
    # print("Es dürfen nur Buchstaben angegeben werden, andere Zeichen werden als Versuch gewertet")


    while True:
            letter = str(input("Geben Sie hier ihren Buchstaben ein: ")) # Eingabe des Buchstaben
            letter = letter.lower() # Alle Buchstaben werden klein geschrieben

            # Überprüfung ob es sich nur um einen Buchstaben handelt
            if len(letter) != 1: 
                print("Die Eingabe enthält mehr als ein Buchstabe. Probieren Sie es nocheinmal")

            # Überprüfung ob es sich um ein Sonderzeichen handelt
            for u in special_characters:
                if letter == u:
                    print("Die Eingabe enthält ein Sonderzeichen. Probieren Sie es nocheinmal")
                    break

            # Überprüfung ob es sich um eine Zahl handelt
            for k in numbers:
                if letter == k:
                    print("Die Eingabe enthält eine Zahl. Probieren Sie es nocheinmal")
                    break

            # Aufzählung der schon eingegebenen Buchstaben        
            if len(letter) == 1 and letter != u and letter != k:
                letters.append(letter)
                print("Bereits eingegebene Buchstaben: " + str(set(letters)),"\n")

                # Ausgabe der noch nicht gewählten Buchstaben. Sobald ein Buchstabe gewählt wurde wird er von der Liste entfernt
                for j in range(len(alphabet)):
                    if letter == alphabet[j]:
                        alphabet.remove(letter)
                        print("Das sind die noch zu Verfügung stehenden Buchstaben")
                        print(alphabet, "\n")
                        break

                # Überprüfung der Eingabe mit der Wort
                found = False
                for i in range(len(word)): 
                    if letter == word[i]:
                        result[i] = word[i]
                        found = True

                # Falls es nicht übereinstimmt, wird ein Versuch abgezogen und das Bild gezeichnet
                if not found:
                    count -= 1
                    print("Sie haben noch " + str(count) + " Versuche")
                    draw_hangman(draw_count)
                    draw_count += 1
                print(result)

                # Überprüfung ob Wort und Eingabe zusammenstimmen.
                if word == result:
                    print("Herzlichen Glückwunsch! Sie haben das Wort erraten.")
                    break
                    
                # Wenn die Versuche gleich 0 sind wird die Überprüfung abgebrochen
                if count == 0:
                    print("Sie haben leider verloren")
                    print("Das gesuchte Wort war: " + random_word)
                    break
                
            
    # Überprüfung, ob der Benutzer nochmal spielen möchte oder das Spiel beenden will
    play_again = input("Möchten Sie nochmal spielen? (yes/y/no/n): ").lower()
    if play_again == "no" or play_again == "n":
        print("Vielen Dank fürs Spielen. Auf Wiedersehen!")
        break
    elif play_again == "yes" or play_again == "y":
        print("Neues Spiel wird gestartet...\n")
        continue
    else:
        print("Ungültige Eingabe. Bitte nur 'yes/y' oder 'no/n' eingeben.\n")
    if play_again == "nein":
        break
            
'''
Erledigt: Überprüfung auf gültige Eingabe: Stelle sicher, dass der Benutzer nur einzelne Buchstaben eingibt und dass der eingegebene Buchstabe noch nicht zuvor erraten wurde.

Erledigt: Anzeige der bereits geratenen Buchstaben: Füge eine Liste hinzu, um die bereits geratenen Buchstaben anzuzeigen.

Erledigt: Anzeige der verbleibenden Buchstaben: Zeige dem Benutzer, welche Buchstaben noch nicht erraten wurden.

Erledigt: Fehlermeldung für ungültige Eingabe: Wenn der Benutzer eine ungültige Eingabe macht (z. B. ein Sonderzeichen), gib eine Fehlermeldung aus und ziehe keinen Versuch ab.

Erledigt: Schleife für mehrere Runden: Lasse den Benutzer so lange weiterspielen, bis er das Spiel beenden möchte oder bis ihm die Versuche ausgehen.

Erledigt: Schwierigkeitsgrad: Füge verschiedene Schwierigkeitsgrade hinzu, z. B. leicht (mehr Versuche), mittel (Standard) und schwer (weniger Versuche).

Offen: Hangman in ein UI interface übertragen.
'''