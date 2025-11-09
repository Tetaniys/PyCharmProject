from colorama import Fore, Back, Style


def draw_board(board):
    n = len(board)
    print('-'*3*n)
    for i in range(n):
        print(' | '.join(board[i]))
        print('-'*3*n)


def ask_and_make_move(player, board):
    x, y = ask_move(player, board)
    make_move(player, board, x, y)


def ask_move(player, board):
    print('Enter the coordinates')
    while True:
        try:
            x, y = input(f"{player}, enter x and y coordinates (e.g. 0 0): ").strip().split()
            x, y = int(x), int(y)
            if (0 <= x <= 2) and (0 <= y <= 2):
                if board[x][y] == ' ':
                    return x, y
                else:
                    print('That spot is already taken. Select a different filed')
            else:
                print('Coordinates must be between 0 and 2. Try again')
        except ValueError:
            print('Please enter two numbers separated by space.')


def make_move(player, board, x, y):
    board[x][y] = player


def check_win(player, board):
    for i in range(3):
        flag_horizontal = 0
        for j in range(3):
            if board[i][j] == player:
                flag_horizontal += 1
        if flag_horizontal == 3:
            return True

    for i in range(3):
        flag_vertical = 0
        for j in range(3):
            if board[j][i] == player:
                flag_vertical += 1
        if flag_vertical == 3:
            return True

    flag_diagonal_1 = 0
    for i in range(3):
        if board[i][i] == player:
            flag_diagonal_1 += 1

    flag_diagonal_2 = 0
    for i in range(3):
        if board[2-i][i] == player:
            flag_diagonal_2 += 1

    if flag_diagonal_1 == 3 or flag_diagonal_2 == 3:
        return True
    else:
        return False


def tic_tac_toe():
    board = [
        [' ', ' ', ' '],
        [' ', ' ', ' '],
        [' ', ' ', ' ']
    ]
    player_1 = 'X'
    player_2 = '0'
    for i in range(9):      # For board 3*3
        draw_board(board)
        current_player = player_1 if i%2 == 0 else player_2
        ask_and_make_move(current_player, board)
        if check_win(player_1, board):
            draw_board(board)
            print(f'{current_player} wins!')
            return

    draw_board(board)
    print('Drawn. Friends are win')


tic_tac_toe()