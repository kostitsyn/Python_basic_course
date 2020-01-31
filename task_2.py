with open('text_2.txt', 'r', encoding='utf-8') as f:

    for num, line in enumerate(f, 1):
        if len(line.split()) != 0:
            line_list = list(line)
            line_list.pop(-1)
            line_str = ''.join(line_list)
            print(f'{line_str}: {len(line_str.split())} слов; символов {len(line_str)}')

    print(f'Всего {num} строк')

