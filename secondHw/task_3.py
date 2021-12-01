#use list
winter = 'winter'
spring = 'spring'
summer = 'summer'
autumn = 'autumn'
months = [winter, winter, spring, spring, spring, summer, summer, summer, autumn, autumn, autumn, winter]
user_input = int(input('Enter number of month: ')) - 1

print('match range[1; 12]') if user_input < 0 or user_input > 11 else print(months[user_input])
