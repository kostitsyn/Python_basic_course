my_list = [8, 7, 6, 6, 5, 2, 1]
input_num = input('Введите число: ')

if int(input_num) in my_list:
    for i, j in enumerate(my_list):
        if j == int(input_num):
            index = i + 1
    my_list.insert(index, input_num)


else:
    if int(input_num) > my_list[0]:
        my_list.insert(0, input_num)
    else:
        for i, j in enumerate(my_list):
            if j < int(input_num):
                index = i - 1
        my_list.insert(index, input_num)

print(my_list)
