class MyError(Exception):
    def __init__(self, txt):
        self.txt = txt


class Date:
    def __init__(self, str_date):
        Date.str_date = str_date

    @classmethod
    def method_1(cls):
        Date.list_date = list(map(int, (cls.str_date).split('-')))
        return Date.list_date

    @staticmethod
    def method_2():
        try:
            Date.method_1()
            if int(Date.list_date[0]) < 0 or int(Date.list_date[0]) > 31 or int(Date.list_date[1]) < 0 or int(
                    Date.list_date[1]) > 12 or int(Date.list_date[2]) < 0:
                raise MyError('Некорректное введение даты!')
        except MyError as error:
            print(error)
        else:
            print("Всё верно!")


m_1 = Date('09-12-2020')
Date.method_2()

m_2 = Date('09-55-2020')
Date.method_2()
