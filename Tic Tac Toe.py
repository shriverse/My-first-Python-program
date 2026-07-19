def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_winner(board, p):
    # rows
    for row in board:
        if row.count(p) == 3:
            return True

    # columns
    for c in range(3):
        if all(board[r][c] == p for r in range(3)):
            return True

    # diagonals
    if all(board[i][i] == p for i in range(3)):
        return True
    if all(board[i][2-i] == p for i in range(3)):
        return True

    return False

board = [[' ']*3 for _ in range(3)]
player = 'X'

for turn in range(9):
    print_board(board)
    r = int(input("Row (0-2): "))
    c = int(input("Col (0-2): "))

    if board[r][c] == ' ':
        board[r][c] = player

        if check_winner(board, player):
            print_board(board)
            print(player, "wins!")
            break

        player = 'O' if player == 'X' else 'X'
else:
    print_board(board)
    print("Draw!")