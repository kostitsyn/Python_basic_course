"""Использовал новую фичу с f-строками, введеную с Python 3.8 {param=}"""

print((lambda name, surname, year, city, email, phone: f'{name=}, {surname=}, {year=}, {city=}, {email=}, {phone=}')
      ('Vasylyi', 'Pupkin', '1917', 'New York', 'pupkin.vas@mail.ru', '890001010'))
