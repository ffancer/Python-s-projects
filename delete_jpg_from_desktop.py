import os
import pathlib

path = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')


files_in_directory = os.listdir(path)
filtered_files = [file for file in files_in_directory if file.endswith(".txt")]

for file in filtered_files:
	path_to_file = os.path.join(path, file)
	os.remove(path_to_file)

