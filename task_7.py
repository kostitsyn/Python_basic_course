import json

with open('text_7.txt', 'r', encoding='utf-8') as f:
    firms = []
    profits = []
    for line in f:
        firms.append(line.split()[0])
        firm_list = line.split()
        profit = int(firm_list[2]) - int(firm_list[3])
        profits.append(profit)
    firm_dict = dict(zip(firms, profits))
    profit_sum_list = []
    for i in profits:
        if i > 0:
            profit_sum_list.append(i)

    aver_profit = int(sum(profit_sum_list) / len(profit_sum_list))

    aver_dict = dict(average_profit=aver_profit)
    result_list = [firm_dict, aver_dict]
    print(result_list)

    with open('text_7.json', 'w', encoding='utf-8') as write_f:
        json.dump(result_list, write_f, ensure_ascii=False)
