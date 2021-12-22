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


# with open('fifth-hw/task_4/task_4.txt', 'r', encoding='utf-8') as file:
#     new_doc = [line.split() for line in file.readlines()]
#     for str_list in new_doc:
#         for word in str_list:
#             if word.lower() in numerals:
#                 str_list[str_list.index(word)] = numerals[word.lower()]
                

# with open('fifth-hw/task_4/task_41.txt', 'w', encoding='utf-8') as file:
#     for line in new_doc:
#         line = ' '.join((map(str, line)))
#         print(line, file=file)
