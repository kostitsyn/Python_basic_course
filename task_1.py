import time


class TrafficLight:
    __color = ['красный', 'желтый', 'зеленый']

    def running(self):
        count = 0
        while True:
            print(f"\033[1m\033[31m{self.__color[0]}", end='')
            time.sleep(7)
            print('\r', end='')
            print(f"\033[1m\033[33m{self.__color[1]}", end='')
            time.sleep(2)
            print('\r', end='')
            print(f"\033[1m\033[32m{self.__color[2]}", end='')
            time.sleep(7)
            print('\r', end='')
            if count == 2:
                print('\033[0mЦикл завершен!')
                break
            print(f"\033[1m\033[33m{self.__color[1]}", end='')
            time.sleep(2)
            print('\r', end='')
            count += 1


tr_light_1 = TrafficLight()
tr_light_1.running()
