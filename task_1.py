from sys import argv

try:
    script_name, work_in_hours, rate_in_hour, prize = argv
    try:
        print(f'Заработная плата сотрудника составляет {int(work_in_hours) * int(rate_in_hour) + int(prize)} печенек')
    except ValueError:
        print('Введите числовые значения!')
except ValueError:
    print(
        'Запустите программу в терминале и введите через пробел следующие параметры:\n  -выработка в часах\n  -ставка в час\n  -премия')
