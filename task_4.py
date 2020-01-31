with open('text_4_in.txt', 'r', encoding='utf-8') as f:
    rus = ["Один", "Два", "Три", "Четыре"]
    result_list = []
    for i, j in enumerate(f):
        elem_list = j.split()
        elem_list.insert(0, rus[i])
        elem_list.pop(1)
        elem_str = ' '.join(elem_list)

        result_list.append(elem_str)
    result_str = '\n'.join(result_list)
    with open('text_4_out.txt', 'w', encoding='utf-8') as d:
        d.write(f'{result_str}')
