def sum_num():
    """Суммирует все введенные числа"""
    sum_string = 0
    while True:
        user_str = input("Введите строку чисел, разделенных пробелом, для выхода нажмите 'e': ").split()
        if user_str[-1].lower() == 'e':
            if len(user_str) == 1:
                break
            else:
                user_str.pop(-1)
                for i in user_str:
                    sum_string += float(i)
                break

        for i in user_str:
            sum_string += float(i)
        print(sum_string)
    return sum_string


print(f'Cумма всех введенных чисел равняется {sum_num()}')
