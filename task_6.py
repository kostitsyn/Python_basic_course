a = int(input("Please input athlet's result on the first day, km: "))
b = int(input("Please input finall of athlet's result: "))

num_day = 1

while b >= a - a / 10:
    print(f"{num_day}-й день: {round(a, 2)}")
    a = a + a * 0.1
    num_day = num_day + 1
print(f'Ответ: на {num_day - 1}-й день спортсмен достиг результата - не менее {b} километров.')