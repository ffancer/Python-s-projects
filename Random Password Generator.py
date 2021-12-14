from string import ascii_letters, digits, punctuation
from random import sample

print('Welcome to Password generator version 1.0\nFor quit enter "q"')
symbols = ascii_letters + digits

while True:
    choice = input('Do you want symbols (^&$#@ etc.) in your password? Y/N: ').lower()
    if choice == 'q':
        print('Come back :)')
        break

    length = input('Enter the length of password: ')
    if length == 'q':
        print('Come back :)')
        break


    def pass_generator(symbols, length):
        if choice == 'y':
            symbols += punctuation
        if length.isdigit():
            return ''.join(sample(symbols, int(length)))


    print(pass_generator(symbols, length))
