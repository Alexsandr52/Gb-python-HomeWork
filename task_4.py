user_number = int(input('Enter int number: '))
the_hiest_number = 0

while user_number > 0:
    current_number = user_number % 10

    if current_number > the_hiest_number:
        the_hiest_number = current_number

    user_number = user_number // 10

print(f'the hiest number is {the_hiest_number}')
