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

display_board()

