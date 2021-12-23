numerals = {
    'one': 'один',
    'two': 'два',
    'three': 'три',
    'four': 'четыре'
}

with open('fifth-hw/task_4/task_4.txt', encoding='utf-8') as file, open('fifth-hw/task_4/task_41.txt', 'w', encoding='utf-8') as new_file:
    for line in file.readlines():
        numeral = line.split()
        new_file.write(f'{line.replace(numeral[0], numerals[numeral[0].lower()])}')
