import os

def path_file(file_name):
    path = os.path.join('files', file_name)
    print(f'Путь к файлу {path}')
    base = os.path.basename(path)
    return os.path.splitext(base)[0]

print(f'Имя файла: {path_file("file.txt")}')