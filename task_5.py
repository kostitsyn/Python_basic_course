revenue = int(input("Please input the company's revenue: "))
cost = int(input("Please input the company's cost: "))
profit = revenue - cost
if profit > 0:
    print(f"A company's work is giving profit. The company's profitability equal {round(profit / revenue, 2)}")
    num_worker = int(input('Please enter number of workers: '))
    print(f"A company's profit for one worker equal {round(profit / num_worker, 2)}")
else:
    print("The company works at loss")

