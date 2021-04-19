from itertools import zip_longest

def zip_example(list_1, list_2):
    print(list(zip_longest(list_1,list_2, fillvalue='None')))

list_1 = ['a', 'b', 'c', 'd']
list_2 = ['1', '2', '3']

zip_example(list_1, list_2)
