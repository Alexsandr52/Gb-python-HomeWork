with open('fifth-hw/task_2/text.txt', encoding='utf-8') as file:
    for line in enumerate(file, start=1):
        print(f'String №{line[0]}, Count of words: {len(line[1].split())}, {line[1]}', end=' ')
