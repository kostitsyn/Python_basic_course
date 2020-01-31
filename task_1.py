my_string = True
while my_string:
    my_string = input('Введите строку: ')
    with open('text_1.txt', 'a') as f:
        f.write(f'{my_string}\n')
