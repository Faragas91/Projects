'''
Aufgabe: Der User überlegt sich eine Zahl (1-100)
und das Programm muss diese Zahl erraten

● Das Programm rät eine Zahl und der User muss
angeben, ob die gesuchte Zahl gefunden wurde,
oder ob sie höher/niedriger als die gesuchte Zahl
ist
'''
from random import randint

x = 0
y = 100
count = 0
number = int(input("Geben Sie hier Ihre Zahl ein: "))

while True:
    pc = randint(x, y)
    if number != pc:
            # print("Zahl wurde nicht erraten", pc)
            # new_number = ""
            # new_number = input("Ist die gesuchte Zahl größer (h) oder kleiner (l) als " + str(pc) +  "? Oder f, wenn " + str(pc) +  " die gesuchte Zahl ist. ")
        if number > pc:
            x += 1
            count += 1
        if number < pc:
            y -= 1
            count += 1
            # if new_number == "f" or x == y:
    if number == pc:
        print("Das Programm hat ihre Zahl nach dem ", count, "Versuch erraten")
        break
        

    
    



