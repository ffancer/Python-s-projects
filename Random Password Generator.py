import string
import random


def pass_generator(length):
    symbols = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.sample(symbols, length))


print(pass_generator(20))
print(pass_generator(12))
print(pass_generator(10))
print(pass_generator(8))
print(pass_generator(4))







