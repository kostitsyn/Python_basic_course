class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def count_weight(self):
        print(f'Масса асфальта для заданных размеров равна {int(self._length * self._width * 25 / 1000 * 5)} тонн')


while True:
    try:
        length, width = list(map(int, input('Введите длину и ширину полотна в метрах через пробел: ').split()))
        road_1 = Road(length, width)
        road_1.count_weight()
        break
    except:
        print('Введите два значения: длина и ширина')
