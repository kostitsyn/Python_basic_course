#Первая часть задания
num_products = int(input('Введите количество товаров: '))

keys = ['название', 'цена', 'количество', 'ед']
values = []
result_values = list()
counter = 1
while counter <= num_products:
    print(f'Заполните характеристики товара {counter}')
    for i in keys:
        param = input(f'Введите {i}: ')
        values.append(param)
    copy_values = values.copy()
    result_values.append(copy_values)
    values.clear()
    counter += 1

result_string = []
for i, j in enumerate(result_values, 1):
    prod_dict = dict(zip(keys, j))
    tuple_prod = tuple([i, prod_dict])
    result_string.append(tuple_prod)
# Вывод списка на экран в одну строку
print(result_string)
#Вывод списка на экран поэлементно
for i in result_string:
    print(i)


#Вторая часть задания

pt = []
union_char = []
counter = 0
while counter < len(keys):
    for i in result_values:
        char = i[counter]
        pt.append(char)
    copy_pt = pt.copy()
    union_char.append(copy_pt)
    pt.clear()
    counter += 1

analitic_dict = dict(zip(keys, union_char))

for i, j in enumerate(union_char[-1]):
    if union_char[-1][0] == union_char[-1][i]:
        union_char[-1].remove(j)
#Вывод словаря на экран в одну строку
print(analitic_dict)
#Вывод словаря на экран поэлементно
for i, j in analitic_dict.items():
    print(i,':', j)


