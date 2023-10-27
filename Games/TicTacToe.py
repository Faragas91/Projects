import numpy as np

board = np.full((3, 3), "_", dtype=str)

## Spielfeld
# [['1' '2' '3']
#  ['4' '5' '6']
#  ['7' '8' '9']]

def winner(symbol):
    
    # Horizontal
    if board[0,0] == symbol and board[0,1] == symbol and board[0,2] == symbol or board[1,0] == symbol and board[1,1] == symbol and board[1,2] == symbol or board[2,0] == symbol and board[2,1] == symbol and board[2,2] == symbol:
        print("Spieler 1 hat gewonnen")
        return True

    # Vertikal
    if board[0,0] == symbol and board[1,0] == symbol and board[2,0] == symbol or board[0,1] == symbol and board[1,1] == symbol and board[2,1] == symbol or board[0,2] == symbol and board[1,2] == symbol and board[2,2] == symbol:
        print("Spieler 1 hat gewonnen")
        return True
  
    # Diagonal
    if board[0,0] == symbol and board[1,1] == symbol and board[2,2] == symbol or board[0,2] == symbol and board[1,1] == symbol and board[2,0] == symbol:
        print("Spieler 1 hat gewonnen")
        return True
    
count = 0
while count <= 9:
    while True:
        player_1 = int(input("Spieler 1 bitte geben Sie hier das Feld ein das sie befüllen möchten: "))
        if player_1 == 1:
            if board[0,0] != "O":
                board[0,0] = "X"
                count += 1
                break
            else: 
                print("Das Feld ist schon belegt")
        if player_1 == 2:
            if board[0,1] != "O":
                board[0,1] = "X"
                count += 1
                break
            else: 
                print("Das Feld ist schon belegt")
        if player_1 == 3:
            if board[0,2] != "O":
                board[0,2] = "X"
                count += 1
                break
            else: 
                print("Das Feld ist schon belegt")
        if player_1 == 4:
            if board[1,0] != "O":
                board[1,0] = "X"
                count += 1
                break
            else: 
                print("Das Feld ist schon belegt")
        if player_1 == 5:
            if board[1,1] != "O":
                board[1,1] = "X"
                count += 1
                break
            else: 
                print("Das Feld ist schon belegt")
        if player_1 == 6:
            if board[1,2] != "O":
                board[1,2] = "X"
                count += 1
                break
            else: 
                print("Das Feld ist schon belegt")
        if player_1 == 7:
            if board[2,0] != "O":
                board[2,0] = "X"
                count += 1
                break
            else: 
                print("Das Feld ist schon belegt")
        if player_1 == 8:
            if board[2,1] != "O":
                board[2,1] = "X"
                count += 1
                break
            else: 
                print("Das Feld ist schon belegt")
        if player_1 == 9:
            if board[2,2] != "O":
                board[2,2] = "X"
                count += 1
                break
            else: 
                print("Das Feld ist schon belegt")

    print(board)

    if winner("X") == True or winner("O") == True:
        break

    while True:
        player_2 = int(input("Spieler 2 bitte geben Sie hier das Feld ein das sie befüllen möchten: "))
        if player_1 == 1:
            if board[0,0] != "X":
                board[0,0] = "O"
                count += 1
                break
            else: 
                print("Das Feld ist schon belegt")
        if player_2 == 2:
            if board[0,1] != "X":
                board[0,1] = "O"
                count += 1
                break
            else: 
                print("Das Feld ist schon belegt")
        if player_2 == 3:
            if board[0,2] != "X":
                board[0,2] = "O"
                count += 1
                break
            else: 
                print("Das Feld ist schon belegt")
        if player_2 == 4:
            if board[1,0] != "X":
                board[1,0] = "O"
                count += 1
                break
            else: 
                print("Das Feld ist schon belegt")
        if player_2 == 5:
            if board[1,1] != "X":
                board[1,1] = "O"
                count += 1
                break
            else: 
                print("Das Feld ist schon belegt")
        if player_2 == 6:
            if board[1,2] != "X":
                board[1,2] = "O"
                count += 1
                break
            else: 
                print("Das Feld ist schon belegt")
        if player_2 == 7:
            if board[2,0] != "X":
                board[2,0] = "O"
                count += 1
                break
            else: 
                print("Das Feld ist schon belegt")
        if player_2 == 8:
            if board[2,1] != "X":
                board[2,1] = "O"
                count += 1
                break
            else: 
                print("Das Feld ist schon belegt")
        if player_2 == 9:
            if board[2,2] != "X":
                board[2,2] = "O"
                count += 1
                break
            else: 
                print("Das Feld ist schon belegt")
    
    print(board)

    if winner("X") == True or winner("O") == True:
        break
        
    