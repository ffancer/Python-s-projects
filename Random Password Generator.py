from string import ascii_letters, digits, punctuation
from random import sample


def pass_generator(length):
    symbols = ascii_letters + digits + punctuation
    return ''.join(sample(symbols, length))


print(pass_generator(20))
print(pass_generator(12))
print(pass_generator(10))
print(pass_generator(8))
print(pass_generator(4))







