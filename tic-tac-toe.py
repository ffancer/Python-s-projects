from random import randint
from time import sleep

# board = ['1', '2', '3',
#          '4', '5', '6',
#          '7', '8', '9'
#          ]
board = '123456789'


def show_board():
    print(f'{board[0]} | {board[1]} | {board[2]}')
    print(f'{board[3]} | {board[4]} | {board[5]}')
    print(f'{board[6]} | {board[7]} | {board[8]}')


# show_board()


# flag = True
# while flag:
#     computer_num = str(randint(1, 9))
#     if computer_num in board:
#         board = board.replace(computer_num, 'X')
#     show_board()
#     sleep(1)
#     if board[0] == board[1] == board[2] or board[0] == board[4] == board[8] or \
#             board[3] == board[4] == board[5] or board[6] == board[7] == board[8] or \
#             board[6] == board[4] == board[2]:
#         print('You win')
#         flag = False


# flag = True
# while flag:
#     num = input('num: ')
#     if num in board:
#         board = board.replace(num, 'X')
#     show_board()
#     if board[0] == board[1] == board[2] or board[0] == board[4] == board[8] or \
#             board[3] == board[4] == board[5] or board[6] == board[7] == board[8] or \
#             board[6] == board[4] == board[2]:
#         print('You win')
#         flag = False


# def player_turn():
#     global board
#     num = input('num: ')
#
#     if num in board:
#         board = board.replace(num, 'X')
#
#     show_board()
#     if board[0] == board[1] == board[2] or board[0] == board[4] == board[8] or \
#             board[3] == board[4] == board[5] or board[6] == board[7] == board[8] or \
#             board[6] == board[4] == board[2]:
#         return 'You win'
#     return 'next turn'


# def computer_turn():
#     computer_num = str(randint(1, 9))
#     if computer_num in board:
#         board = board.replace(computer_num, 'O')


# while True:
#     if player_turn() == 'You win':
#         print('You win')
#         break
#     print(player_turn())


class Turn():
    def __init__(self):
        self.player_turn = input('Your turn: ')
        self.sign = 'X'

        if self.player_turn in '123456789':
            board = '123456789'
            board = board.replace(self.player_turn, self.sign)

            def show_board():
                print(f'{board[0]} | {board[1]} | {board[2]}')
                print(f'{board[3]} | {board[4]} | {board[5]}')
                print(f'{board[6]} | {board[7]} | {board[8]}')

            show_board()
        else:
            print('not correct')


while True:
    Turn()
