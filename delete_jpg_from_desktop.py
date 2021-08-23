import os

path = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
files_in_directory = os.listdir(path)


def delete_files(type_files='.txt'):
    filtered_files = [file for file in files_in_directory if file.endswith(type_files)]

    for file in filtered_files:
        path_to_file = os.path.join(path, file)
        os.remove(path_to_file)


delete_files()
delete_files('jpg')
delete_files('png')
