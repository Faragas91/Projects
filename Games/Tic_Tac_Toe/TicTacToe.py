import numpy as np

board = np.full((3, 3), "_", dtype=str)
print(board)
count = 0

## Spielfeld
# [['1' '2' '3']
#  ['4' '5' '6']
#  ['7' '8' '9']]

def winner(player, symbol):
    
    # Horizontal
    if board[0,0] == symbol and board[0,1] == symbol and board[0,2] == symbol or board[1,0] == symbol and board[1,1] == symbol and board[1,2] == symbol or board[2,0] == symbol and board[2,1] == symbol and board[2,2] == symbol:
        print(player + " Win")
        return True

    # Vertikal
    if board[0,0] == symbol and board[1,0] == symbol and board[2,0] == symbol or board[0,1] == symbol and board[1,1] == symbol and board[2,1] == symbol or board[0,2] == symbol and board[1,2] == symbol and board[2,2] == symbol:
        print(player + " Win")
        return True
  
    # Diagonal
    if board[0,0] == symbol and board[1,1] == symbol and board[2,2] == symbol or board[0,2] == symbol and board[1,1] == symbol and board[2,0] == symbol:
        print(player + " Win")
        return True

    if np.all(board != "_"):
        print("Tie")
        return True
    


def set_symbol(player, symbol):
    while True:
        field = int(input(f"{player} please enter the field you would like to fill in here: "))
        row, col = divmod(field - 1, 3)
        if 1 <= field <= 9 and board[row, col] == "_":
            board[row, col] = symbol
            break
        else:
            print("Invalid entry or the field is already filled.")

def draw(player, symbol):
    global count
    set_symbol(player, symbol)
    count +=1
    print(board)
    if winner(player, symbol):
        return True
    return False

while True:
    while count <= 9:
        if draw("Player 1", "X"):
            break
        if draw("Player 2", "O"):
            break

# Überprüfung, ob der Benutzer nochmal spielen möchte oder das Spiel beenden will
    play_again = input("Do you want to play again? (yes/y/no/n): ").lower()
    if play_again == "no" or play_again == "n":
        print("Thank you for playing, Good Bye!")
        break
    elif play_again == "yes" or play_again == "y":
        print("New game will startet...\n")
        board = np.full((3, 3), "_", dtype=str)
        print(board)
        count = 0
        continue
    else:
        print("Invalid entry. Please use 'yes/y' or 'no/n'.\n")
    if play_again == "nein":
        break
    


