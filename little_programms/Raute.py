# Erstellen Sie ein Programm, dass eine
# Raute auf der Konsole ausgibt.
# Eingabe: Seitenlänge (beliebige positive ganze Zahl größer/gleich 1)
# Ausgabe: Raute aus *
# Zeichen wird auf der Konsole ausgegeben, wobei die Seitenlänge der
# Raute der eingegebenen Seitenlänge entspricht


def rautezeichnen(seitenlänge):
    stern = "*"
    leerzeichen = " "

    i = 0
    while i <= seitenlänge: 
        print((leerzeichen * (seitenlänge - i)) + (stern * (2 * i + 1) + (leerzeichen * (seitenlänge - i))))
        i += 1

    j = seitenlänge - 1
    while j >= 0: 
        print((leerzeichen * (seitenlänge - j)) + (stern * (2 * j + 1) + (leerzeichen * (seitenlänge - j))))
        j -= 1

seitenlänge = int(input("Geben Sie hier ihre Seitenlänge ein: "))

rautezeichnen(seitenlänge)