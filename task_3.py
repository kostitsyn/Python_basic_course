class Worker:
    def __init__(self, name, surname, position, income={"wage": 20, "bonus": 10}):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = income


class Position(Worker):
    def get_full_name(self):
        print(f"Работника зовут {self.name} {self.surname}")

    def get_total_income(self):
        sum_prof = sum(self._income.values())
        print(f'Он зарабатывает {sum_prof} печенек')


human_1 = Position('Vasilyi', 'Pupkin', 'Developer')
human_1.get_full_name()
print(human_1.name)
print(human_1.surname)
print(human_1.position)
print(human_1._income)
human_1.get_total_income()
