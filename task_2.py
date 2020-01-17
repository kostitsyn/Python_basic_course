enter_sec = int(input('Please input seconds: '))

hours = enter_sec // (60 * 60)
min = (enter_sec - hours * (60 * 60)) // 60
sec = enter_sec % 60

print(f'Your seconds equals {hours:02}:{min:02}:{sec:02}')