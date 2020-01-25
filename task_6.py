from sys import argv
import itertools

try:
    iter_name = argv[1]
    if iter_name == 'count':
        try:
            number = int(argv[2])
            step = int(argv[3])
            for i in itertools.count(number, step):
                if i > number + 20:
                    break
                print(i)
        except IndexError:
            print(
                'Введите через пробел два числа:\nпервое - число, с которого начнется отсчет'
                '\nвторое - шаг, с которым будет идти отсчет')


    elif iter_name == 'cycle':
        try:
            number_list = list(map(int, argv[2].split(',')))
            counter = 0
            for i in itertools.cycle(number_list):
                print(i)
                if counter > 5:
                    break
                counter += 1
        except IndexError:
            print('Введите последовательность чисел, разделенных запятой без пробела')
except ValueError:
    print('Нужно ввести числа!')
except IndexError:
    print(
        'Запустите программу в терминале и введите название команды:\n count - генерация целого числа, начиная с указанного'
        '\n cycle - повторение элементов списка')
