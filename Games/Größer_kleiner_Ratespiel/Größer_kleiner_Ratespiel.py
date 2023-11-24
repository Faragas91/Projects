# – Programm wählt eine Zufallszahl zw. 1 und 10

# – User darf so lange raten bis die richtige Zahl gefunden ist

# – Programm teilt mit, ob eingegebene Zahl größer od. kleiner als die Zufallszahl ist


from random import randint

while True:
    x = int(input("Geben sie hier ihre Zahl ein: "))

    if x <= 0 or x >= 11:
        print("Ihre Zahl ist nicht zwischen 1 und 10")
        continue

    y = randint(1, 10)

    if x == y:
        print("Die Zahlen sind gleich")
        break

    elif x <= y:
        print("Ihr Zahl " + str(x) + " ist kleiner als " + str(y))
        print("Versuch es nochmal")

    elif x >= y:
        print("Ihr Zahl " + str(x) + " ist größer als " + str(y))
        print("Versuch es nochmal")