# Tic-Tac-Toe

board = []
playing = True
player1 = True

def init_board():
    # 3 x 3 Matrix (Tabelle)
    for m in range(0, 4):
        temp = []
        for n in range (0, 4):
            if m == 0:
                temp.append(n)
            else:
                if n == 0:
                    temp.append(m)
                else:
                    temp.append(".")
        board.append(temp)

def display_board():
    print("SPIELFELD")
    print("#########")
    for liste in board:
        for element in liste:
            print(element, end=" ")
        print()

def has_hor_winner(symbol, row, col):
    ## [1][1] and [1][2] and [1][3]
    ## [2][1] and [2][2] and [2][3]
    ## [3][1] and [3][2] and [3][3]
    ## zusammengefasst: 1 innere Liste muss von Index 1 - 3 gleiche Zeichen enthalten (X oder O)
    return False # True, wenn Sieger!

def has_ver_winner(symbol, row, col):
    ## [1][1] and [2][1] and [3][1]
    ## [1][2] and [2][2] and [3][2]
    ## [1][3] and [2][3] and [3][3]
    ## zusammengefasst: wenn für jede innere Liste, beim gleichen Index das gleiche Zeichen gesetzt wurde(X oder O)
    return False # True, wenn Sieger!

def has_dia_winner(symbol, row, col):
    ## [1][1] and [2][2] and [3][3]
    ## [1][3] and [2][2] and [3][1]
    ## zusammengefasst: [2][2] muss immer mit gleichem Zeichen (X oder O) versehen sein UND gesonderte Teilbedingungen
    return False # True, wenn Sieger!

init_board()
display_board()

while(playing):
    if player1:
        print("Spieler 1 (X) am Zug:")
        print("---------------------")
        try:
            row = int(input("Zeile eingeben (1-3): "))
            if row < 1 or row > 3:
                print("Bitte eine Zahl zwischen 1-3 eingeben!")
                continue
        except:
            print("Bitte eine Zahl zwischen 1-3 eingeben!")
            continue
        
        try:
            col = int(input("Spalte eingeben (1-3): "))
            if col < 1 or col > 3:
                print("Bitte eine Zahl zwischen 1-3 eingeben!")
                continue
        except:
            print("Bitte eine Zahl zwischen 1-3 eingeben!")
            continue
        print()
        if board[row][col] == ".":
            board[row][col] = "X"
            display_board()
        else:
            print("Feld bereits belegt!")
        if has_hor_winner("X", row, col) or has_ver_winner("X", row, col) or has_dia_winner("X", row, col):
            print("Glückwunsch, Spieler 1... du hast gewonnen!")
            break
        player1 = False
    else:
        print("Spieler 2 (O) am Zug:")
        print("---------------------")
        try:
            row = int(input("Zeile eingeben (1-3): "))
            if row < 1 or row > 3:
                print("Bitte eine Zahl zwischen 1-3 eingeben!")
                continue
        except:
            print("Bitte eine Zahl zwischen 1-3 eingeben!")
            continue
        
        try:
            col = int(input("Spalte eingeben (1-3): "))
            if col < 1 or col > 3:
                print("Bitte eine Zahl zwischen 1-3 eingeben!")
                continue
        except:
            print("Bitte eine Zahl zwischen 1-3 eingeben!")
            continue
        print()
        if board[row][col] == ".":
            board[row][col] = "O"
            display_board()
        else:
            print("Feld bereits belegt!")
        if has_hor_winner("O", row, col) or has_ver_winner("O", row, col) or has_dia_winner("O", row, col):
            print("Glückwunsch, Spieler 1... du hast gewonnen!")
            break
        player1 = True

# Siegesbedingung bzgl. X oder O:
# 1. Horizontal: Komplette Zeile voll 
# 2. Vertikal: Komplette Spalte voll
# 3. Diagonal: Komplette Diagonale voll

# 1.: 
## [1][1] and [1][2] and [1][3]
## [2][1] and [2][2] and [2][3]
## [3][1] and [3][2] and [3][3]
## zusammengefasst: 1 innere Liste muss von Index 1 - 3 gleiche Zeichen enthalten (X oder O)

# 2.:
## [1][1] and [2][1] and [3][1]
## [1][2] and [2][2] and [3][2]
## [1][3] and [2][3] and [3][3]
## zusammengefasst: wenn für jede innere Liste, beim gleichen Index das gleiche Zeichen gesetzt wurde(X oder O)

# 3.:
## [1][1] and [2][2] and [3][3]
## [1][3] and [2][2] and [3][1]
## zusammengefasst: [2][2] muss immer mit gleichem Zeichen (X oder O) versehen sein UND gesonderte Teilbedingungen



