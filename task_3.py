class MyError(Exception):
    def __init__(self, txt):
        self.txt = txt


my_list = []
while True:
    try:
        num_list = input('Введите целое положительное число, для выхода введите stop: ')
        if num_list == 'stop':
            break
        if num_list.isdigit():
            pass
        else:
            raise MyError('Вводите только целые положительные числа!')
    except MyError as error:
        print(error)
    else:
        my_list.append(int(num_list))
print(f'Список введенных чисел{my_list}')
