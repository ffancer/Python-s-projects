import os
import pathlib

path = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
file = 'test2.txt'

file = pathlib.Path(path + "/test.txt")
file.unlink()

