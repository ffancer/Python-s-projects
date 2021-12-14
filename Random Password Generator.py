from string import ascii_letters, digits, punctuation
from random import sample

print('Welcome to Password generator version 1.0\nFor quit enter "q"')
symbols = ascii_letters + digits + punctuation

while True:
    length = input('Enter the length of password: ')
    if length == 'q':
        print('Come back :)')
        break
    elif length.isdigit():
        print(''.join(sample(symbols, int(length))))
    else:
        continue




