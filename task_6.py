with open('text_6.txt', 'r', encoding='utf-8') as f:
    enter_list = f.readlines()
    subjects = []
    hours = []
    for i in enter_list:
        hours.append(i.split()[0])
        elem_list = i.split()[1:]
        while elem_list.count('-'):
            elem_list.remove('-')
        hours_list = []
        for j in elem_list:
            div_list = j.split('(')
            hours_list.append(int(div_list[0]))
        sum_hours = sum(hours_list)
        subjects.append(sum_hours)
    res_dict = dict(zip(hours, subjects))
    print(res_dict)
