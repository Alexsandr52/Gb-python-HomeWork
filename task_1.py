# simple calculator

print('Welcome to my calculator \nhere you can do multiple operations between numbers')
print('lat\'s start')
print('operations: \'+\', \'-\', \'*\', \'/\' ')
print('numbers format: int')
repeat = 'y'

while repeat == 'y':
    operation = input('input operation that you need to do: ')
    if operation != '+' and operation != '-' and operation != '*' and operation != '/':
        print('the operation is not correct')
        repeat = input('try again? |y/n|: ')
        continue
    first_num = int(input(f'input first num, (#) {operation} #: '))
    second_num = int(input(f'input second num, {first_num} {operation} (#): '))

    if operation == '+':
        result = first_num + second_num
    elif operation == '-':
        result = first_num - second_num
    elif operation == '*':
        result = first_num * second_num
    elif operation == '/':
        result = first_num / second_num
    else:
        print('something wrong')
        repeat = input('try again? |y/n|: ')
        continue

    print(first_num, operation, second_num, '=', result)
    repeat = input('try again? |y/n|: ')
