months = {
    1: 'January',
    2: 'February',
    3: 'March',
    4: 'April',
    5: 'Мay',
    6: 'June',
    7: 'July',
    8: 'August',
    9: 'September',
    10: 'October',
    11: 'November',
    12: 'December'
}
user_input = int(input('Enter number of month: '))

print('match range[1; 12]') if user_input < 1 or user_input > 12 else print(months[user_input])
