# sum
user_number = input('Enter numder \'n\': ')
result = int(user_number) + int(user_number + user_number) + \
    int(user_number + user_number + user_number)
print(f'{user_number} + {user_number*2} + {user_number*3} = {result}')
