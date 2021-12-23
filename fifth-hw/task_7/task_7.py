import json

with open('fifth-hw/task_7/task_7.txt', encoding='utf-8') as file:
    sum_of_profits = 0
    info_list = [{}]
    counter = 0

    for line in file.readlines():
        line = line.split()
        profit = int(line[2]) - int(line[3])
        if profit > 0:
            sum_of_profits += profit
            counter += 1
        info_list[0].update({f'{line[0]}': profit})
    info_list.append({f'model_profit': sum_of_profits / counter})
    
with open('fifth-hw/task_7/task_7.json', 'w', encoding='utf-8') as js:
    json.dump(info_list, js)
