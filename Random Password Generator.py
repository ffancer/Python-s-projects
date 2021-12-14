from string import ascii_letters, digits, punctuation
from random import sample

print('Welcome to Password generator version 1.0')
symbols = ascii_letters + digits + punctuation

while True:
    length = int(input('Enter the length of password: '))
    print(''.join(sample(symbols, length)))




