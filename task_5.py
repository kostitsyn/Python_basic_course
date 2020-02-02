class Statlonery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print("Запуск отрисовки")


class Pen(Statlonery):
    def draw(self):
        print("Прорисовка ручкой")


class Pencil(Statlonery):
    def draw(self):
        print("Прорисовка карандашом")


class Handle(Statlonery):
    def draw(self):
        print("Прорисовка маркером")


painting = Statlonery("Экземпляр родительского класса")
painting.draw()

painting_pen = Pen('Экземпляр дочернего класса ручка')
painting_pen.draw()

painting_pencil = Pencil('Экземпляр дочернего класса карандаш')
painting_pencil.draw()

painting_handle = Handle('Экземпляр дочернего класса маркер')
painting_handle.draw()
