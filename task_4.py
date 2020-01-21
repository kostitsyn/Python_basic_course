user_string = input('Введите строку, слова разделяют пробелы: ')
user_list = user_string.split()
for i, j in enumerate(user_list, 1):
    if len(j) > 10:
        j = j[:10]
    print(i, j)
