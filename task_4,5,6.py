class Warehouse:
    def __init__(self, num_print, num_scan, num_xerox):
        self.num_print = num_print
        self.num_scan = num_scan
        self.num_xerox = num_xerox

    # Реализация 5-го задания
    def num_office_eq(self):
        return {Printer.type_org: self.num_print, Scanner.type_org: self.num_scan, Xerox.type_org: self.num_xerox}

    def give_division(self, division):
        self.division = division
        for i, list in self.division:
            print(
                f'{i}:\n {int(self.num_print) // list[0]} {Printer.type_org}, {int(self.num_scan) // list[1]} {Scanner.type_org}, {int(self.num_xerox) // list[2]} {Xerox.type_org}')


class Office_eq:
    def __init__(self):
        self.type_paper = 'A4'
        self.year = 2019


class Printer(Office_eq):
    type_org = 'Принтер'

    def __init__(self):
        super().__init__()


class Scanner(Office_eq):
    type_org = 'Сканер'

    def __init__(self):
        super().__init__()


class Xerox(Office_eq):
    type_org = 'Ксерокс'

    def __init__(self):
        super().__init__()


class MyError(Exception):
    def __init__(self, txt):
        self.txt = txt


# Реализация 6-го задания
while True:
    try:
        num_print = input('Введите количество принтеров: ')
        if num_print.isdigit():
            pass
        else:
            raise MyError('Вводите только целые положительные числа!')
    except MyError as error:
        print(error)
    else:
        break

num_scan = input('Введите количество сканеров: ')
num_xerox = input('Введите количество ксероксов: ')
obj_1 = Warehouse(num_print, num_scan, num_xerox)
print(obj_1.num_office_eq())

#Во вложенных списках кратные значения от общего количества оргтехники в каждом подразделении
div = [['Отдел кадров', [4, 3, 2]], ['IT отдел', [3, 6, 3]], ['Канцелярия', [4, 2, 5]]]
obj_1.give_division(div)
