"""
Our algorithm:
1)board 2)display board 3)play game 4)handle turn 5)check win (check rows/columns/diagonals)
6)check tie 7)flip player
"""


# ------ Global Variables ------

# Game board
board = ['-', '-', '-',
         '-', '-', '-',
         '-', '-', '-']

# If game still going
game_still_going = True

# Who win? Or tie?
winner = None


# Who's turn is it
current_player = 'X'


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
    # The game has ended
    if winner == 'X' or winner == 'O':
        print(winner + ' won.')
    elif winner:
        print('Tie.')
def handle_turn(player):
    position = input('Choose position from 1-9: ')
    position = int(position) - 1

    board[position] = 'X'
    display_board()


def check_if_game_over():
    check_for_winner()
    check_if_tie()

def check_for_winner():
    global winner
    # check rows
    row_winner = check_rows()
    # check columns
    column_winner = check_columns()
    # check diagonals
    diagonal_winner = check_diagonals()
    if row_winner:
        winner = row_winner
    elif column_winner:
        winner = column_winner
    elif diagonal_winner:
        winner = diagonal_winner
    else:
        winner = None
    return
def check_rows():
    return
def check_columns():
    return
def check_diagonals():
    return
def check_if_tie():
    return

def flip_player(): # flip X to O
    return


play_game()
