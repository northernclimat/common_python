import random


def print_board(board):
    for row in board:
        print("|", end="")
        for cell in row:
            if cell == 0:
                print(" ", end="")
            elif cell == 1:
                print("X", end="")
            elif cell == -1:
                print("O", end="")
            print("|", end="")
        print("\n" + "-" * 5)


def check_winner(board):
    for row in board:
        if sum(row) == 3:
            return 1
        if sum(row) == -3:
            return -1

    for col in range(3):
        if sum(board[row][col] for row in range(3)) == 3:
            return 1
        if sum(board[row][col] for row in range(3)) == -3:
            return -1

    if sum(board[i][i] for i in range(3)) == 3 or sum(board[i][2 - i] for i in range(3)) == 3:
        return 1
    if sum(board[i][i] for i in range(3)) == -3 or sum(board[i][2 - i] for i in range(3)) == -3:
        return -1

    return 0


def bot_move(board):
    empty_cells = [(i, j) for i in range(3) for j in range(3) if board[i][j] == 0]
    return random.choice(empty_cells)


board = [[0] * 3 for _ in range(3)]
current_player = 1

while True:
    print_board(board)
    if current_player == 1:
        row = int(input("Введите номер строки (0-2): "))
        col = int(input("Введите номер столбца (0-2): "))
        if board[row][col] == 0:
            board[row][col] = 1
        else:
            print("Эта клетка уже занята! Попробуйте еще раз.")
            continue
    else:
        row, col = bot_move(board)
        print(f"Бот делает ход в клетку {row}, {col}.")
        board[row][col] = -1

    winner = check_winner(board)
    if winner != 0:
        print_board(board)
        if winner == 1:
            print("Вы выиграли!")
        else:
            print("Бот выиграл!")
        break

    if all(board[i][j] != 0 for i in range(3) for j in range(3)):
        print_board(board)
        print("Ничья!")
        break

    current_player = -current_player
