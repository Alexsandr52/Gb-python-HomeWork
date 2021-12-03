winter = 'winter'
spring = 'spring'
summer = 'summer'
autumn = 'autumn'

months = {
    1: winter,
    2: winter,
    3: spring,
    4: spring,
    5: spring,
    6: summer,
    7: summer,
    8: summer,
    9: autumn,
    10: autumn,
    11: autumn,
    12: winter
}
user_input = int(input('Enter number of month: '))

print('match range[1; 12]') if user_input < 1 or user_input > 12 else print(months[user_input])
