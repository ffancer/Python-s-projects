"""
Our algorithm:
1)board 2)display board 3)play game 4)handle turn 5)check win (check rows/columns/diagonals)
6)check tie 7)flip player
"""

board = ['-', '-', '-',
         '-', '-', '-',
         '-', '-', '-']


def display_board():
    print(board[0] + ' | ' + board[1] + ' | ' + board[2])
    print(board[3] + ' | ' + board[4] + ' | ' + board[5])
    print(board[6] + ' | ' + board[7] + ' | ' + board[8])


def play_game():
    display_board()
    while game_still_going:
        handle_turn(current_player)
        check_if_game_over()
        flip_player()


def handle_turn():
    position = input('Choose position from 1-9: ')
    position = int(position) - 1

    board[position] = 'X'
    display_board()


play_game()
