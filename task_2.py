class MyError(Exception):
    def __init__(self, txt):
        self.txt = txt


while True:
    try:
        num_1 = int(input("Введите делимое: "))
        num_2 = int(input("Введите делитель: "))
        if num_2 == 0:
            raise MyError('Делить на ноль нельзя!!!')
    except ValueError:
        print('Введите числа!')
    except MyError as error:
        print(error)
    else:
        result = num_1 / num_2
        print(f'{num_1}/{num_2} = {result}')
        break
