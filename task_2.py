from abc import ABC, abstractmethod


class Clothes(ABC):
    def __init__(self, title, V, H):
        self.title = title
        self.V = V
        self.H = H

    @abstractmethod
    def size(self):
        pass

    @abstractmethod
    def height(self):
        pass


class Coat(Clothes):
    @property
    def size(self):
        return round(self.V / 6.5 + 0.5, 2)

    def height(self):
        pass


class Suit(Clothes):
    def size(self):
        pass

    @property
    def height(self):
        return 2 * self.H + 0.3


coat_1 = Coat('Размер', 2, 4)
suit_1 = Suit('Рост', 2, 4)
print(f'Расход ткани для пальто: {coat_1.size}')
print(f'Расход ткани для костюма: {suit_1.height}')
print(f'Общий расход ткани: {round(coat_1.size + suit_1.height, 2)}')
