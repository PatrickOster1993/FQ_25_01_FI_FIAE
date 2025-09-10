# Tic-Tac-Toe

board = []
player1 = True

def init_board():
    # 3 x 3 Matrix (Tabelle)
    global board
    board = []
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

def has_winner(symbol):
    def has_hor_winner(symbol):
        ## [1][1] and [1][2] and [1][3]
        ## [2][1] and [2][2] and [2][3]
        ## [3][1] and [3][2] and [3][3]
        ## zusammengefasst: 1 innere Liste muss von Index 1 - 3 gleiche Zeichen enthalten (X oder O)
        for liste in board:
            if liste[1] == symbol and liste[2] == symbol and liste[3] == symbol:
                return True
        return False

    def has_ver_winner(symbol):
        ## [1][1] and [2][1] and [3][1]
        ## [1][2] and [2][2] and [3][2]
        ## [1][3] and [2][3] and [3][3]
        ## zusammengefasst: wenn für jede innere Liste, beim gleichen Index das gleiche Zeichen gesetzt wurde(X oder O)
        counter_list = [0, 0, 0]
        for m in range(0, 4):
            if board[m][1] == symbol:
                counter_list[0] += 1
            elif board[m][2] == symbol:
                counter_list[1] += 1
            elif board[m][3] == symbol:
                counter_list[2] += 1
        if 3 in counter_list:
            return True
        return False

    def has_dia_winner(symbol):
        ## [1][1] and [2][2] and [3][3]
        ## [1][3] and [2][2] and [3][1]
        ## zusammengefasst: [2][2] muss immer mit gleichem Zeichen (X oder O) versehen sein UND gesonderte Teilbedingungen
        if board[2][2] == symbol:
            if board[1][1] == symbol and board[3][3] == symbol:
                return True
            elif board[1][3] == symbol and board[3][1] == symbol:
                return True
        return False # True, wenn Sieger!
    
    return has_hor_winner(symbol) or has_ver_winner(symbol) or has_dia_winner(symbol)

def is_ocupied():
    for liste in board:
        if "." in liste:
            return False
    print("Spielfeld vollständig belegt - Remis!")
    print()
    return True

init_board()
display_board()

while(True):

    if player1:
        symbol = "X"
        player = 1
    else:
        symbol = "O"
        player = 2

    print(f"Spieler {player} ({symbol}) am Zug:")
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
        board[row][col] = symbol
        display_board()
    else:
        print("Feld bereits belegt!")
        player1 = not player1
    if has_winner(symbol):
        print(f"Glückwunsch, Spieler {player}... du hast gewonnen!")
        break
    if is_ocupied():
        init_board()
        display_board()
        player1 = True
        continue
    player1 = not player1