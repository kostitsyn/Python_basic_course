while True:
    month = int(input('Введите месяц от 1 до 12: '))
    if month < 1 or month > 12:
        continue
    else:
        break

# Решение через list

winter = [1, 2, 12]
spring = [3, 4, 5]
summer = [6, 7, 8]
fall = [9, 10, 11]

if month in winter:
    print('Это зимний месяц')
elif month in spring:
    print('Это весенний месяц')
elif month in summer:
    print('Это летний месяц')
else:
    print('Это осенний месяц')

# Решение через dict

time_year = ['winter', 'spring', 'summer', 'fall']
month_year = [[1, 2, 12], [3, 4, 5], [6, 7, 8], [9, 10, 11]]

month_dict = dict(zip(time_year, month_year))

if month in month_dict.get('winter'):
    print('Это зимний месяц')
elif month in month_dict.get('spring'):
    print('Это весенний месяц')
elif month in month_dict.get('summer'):
    print('Это летний месяц')
else:
    print('Это осенний месяц')
