x = input("Введите число: ")

if '.' in x:
    print(f'Число "{x}" дробное')
    element = x.split('.')
    if element[0] == element[1]:
        print("True")
    else:
        print("False")

else:
    print(f'Число "{x}" целое')