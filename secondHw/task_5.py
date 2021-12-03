my_list = [7, 5, 3, 3, 2]
user_input = int(input('Enter your number: '))
examination = False

for elem in my_list:
    if user_input > elem:
        my_list.insert(my_list.index(elem), user_input)
        examination = True
        break

if not examination:
    my_list.append(user_input)

print(my_list)
