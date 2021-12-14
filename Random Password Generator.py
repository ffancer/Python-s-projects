from string import ascii_letters, digits, punctuation
from random import sample

print('Welcome to Password generator version 1.0\nFor quit enter "q"')
symbols = ascii_letters + digits

while True:
    choice = input('Do you want symbols (^&$#@ etc.) in your password? Y/N: ').lower()
    length = input('Enter the length of password: ')
    if choice == 'y':
        symbols += punctuation
        if length == 'q':
            print('Come back :)')
            break
        elif length.isdigit():
            print(''.join(sample(symbols, int(length))))
        else:
            continue
    elif choice == 'n':
        if length == 'q':
            print('Come back :)')
            break
        elif length.isdigit():
            print(''.join(sample(symbols, int(length))))
        else:
            continue





