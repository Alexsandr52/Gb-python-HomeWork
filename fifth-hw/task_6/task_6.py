results = dict()
with open('fifth-hw/task_6/task_6.txt', encoding='utf-8') as file:
    for line in file.readlines():
        line = line.split()
        sum_of_hours = 0
        for element in line[1:]:
            number = '0'
            for el in element:
                if el.isdigit():
                    number += el 
            sum_of_hours += int(number)
        results.update({line[0].strip(':'): sum_of_hours})
    print(results)