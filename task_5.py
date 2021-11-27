revenue_value = float(input('revenue value: '))
cost_value = float(input('cost value: '))

if revenue_value > cost_value:
    profit = revenue_value - cost_value
    print('the company works for "profit"')

    profitability_of_proceeds = profit / revenue_value
    print(f'profitability of proceeds {profitability_of_proceeds}')

    workers_num = int(input('number of employees: '))
    print(f'profit per employee {profit/workers_num}')
else:
    print('the company is operating at a "loss"')
