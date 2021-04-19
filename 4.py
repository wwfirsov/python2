import os
from itertools import zip_longest
import string
import random

def txt_file():
    if os.path.isfile('file.txt'):
        print('Такой файл уже существует!')
    else:
        with open('file.txt', 'w', encoding='utf-8') as g:
            list_text = [random.choice(string.ascii_letters) for i in range(7)]
            list_int = [i for i in range(7)]
            dict = list(zip_longest(list_text, list_int, fillvalue='None'))
            for i in dict:
                g.write(str(i))
                g.write('\n')
        g.close()
        path_file = os.path.join('file.txt')

    path_file_fn(path_file)
    return path_file

def path_file_fn(path_file):
    f = open(path_file, 'r', encoding='UTF-8')
    print(f.readlines())
    f.close()

txt_file()




