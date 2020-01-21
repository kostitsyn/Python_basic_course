user_list = []
lenght_list = int(input("Введите требуемую длину списка: "))
while lenght_list:
    num_element = input('Введите элемент списка: ')
    user_list.append(num_element)
    lenght_list -= 1

result_list = []
while len(user_list):
    slice = user_list[:2]
    if len(slice) >= 2:
        var_1, var_2 = slice
        var_2, var_1 = var_1, var_2
        for i in slice:
            user_list.pop(0)
        result_list.append(var_1)
        result_list.append(var_2)
    else:
        result_list.append(slice[0])
        user_list.pop(0)
print(result_list)
