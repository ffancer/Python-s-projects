import os

path = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
file = 'test2.txt'

with open(os.path.join(path, file), 'w') as fp:
    pass
