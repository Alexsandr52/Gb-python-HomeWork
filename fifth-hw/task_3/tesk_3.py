with open('fifth-hw/task_3/task_3.txt', encoding='utf-8') as file:
    low_salary = [line.split()[0] for line in file.readlines() if int(line.split()[1]) <= 20000 ]
    print(low_salary)
    #Не понял строчку 'Выполнить подсчет средней величины дохода сотрудников.', поэтому выполнил для всех.
    file.seek(0)
    salaris = [line.split()[1] for line in file.readlines()]
    salaris = sum(list(map(int, salaris)))/len(salaris)
    print(f'midel salary {salaris}')