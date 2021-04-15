import os
from itertools import zip_longest
import string
import random

def txt_file():
    if os.path.isfile('file.txt'):
        print('Такой файл уже существует!')
    else:
        with open('file.txt', 'w', encoding='utf-8') as g:
            #list_text = ['a', 'b', 'c', 'd', 'i', 'f']
            list_text = [random.choice(string.ascii_letters) for i in range(7)]
            list_int = [i for i in range(7)]
            dict = list(zip_longest(list_text, list_int, fillvalue='None'))
            print('Каталог: ', dict)
            for i in dict:
                print('Значение i: ', i)
                g.write(str(i))
                g.write('\n')


txt_file()




