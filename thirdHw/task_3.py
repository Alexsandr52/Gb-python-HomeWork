def my_func(*args):
    return sum(sorted(args)[-2:])

first_num = input('Enter first nuber: ')
second_num = input('Enter second nuber: ')
third_num = input('Enter third nuber: ')

user_input_list = list(map(float, [first_num, second_num, third_num]))

print(my_func(user_input_list[0], user_input_list[1], user_input_list[2]))
