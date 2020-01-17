input_num = int(input('Please enter number: '))
coef = 10
max_num = 0
while True:
    dischar_num = int(input_num % coef)
    current_num = int(dischar_num / int(coef / 10))
    if current_num == 9:
        max_num = current_num
        break
    input_num = input_num - dischar_num
    next_num = int((input_num % (coef * 10)) / coef)
    if next_num == 0:
        break
    # if coef == 10:
    #     print(current_num)
    #     print(next_num)
    # else:
    #     print(next_num)
    if coef == 10:
        max_num = current_num
    if max_num < next_num:
        max_num = next_num
    coef = coef * 10

print(f'Max num equals {max_num}')

