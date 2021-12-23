with open('fifth-hw/task_1/userfile.txt', 'w') as user_file:
    while True:
        user_input = input('Enter your str: ')
        if len(user_input.split()) == 0:
            break
        print(user_input, file = user_file)
# В моем редакторе запуск происходит из корневой папки, поэтому приходится 
# указывать относительный путь к фаелу. Так во всех 7 задачах.)
