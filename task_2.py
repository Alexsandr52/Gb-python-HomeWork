class ZeroDivisionException(Exception):

    def __init__(self, text):
        self.text = text

try:
    users_numbers = list(map(float, input('Enter tow numbers separated by a space: ').split()))
    if users_numbers[1] == 0:
        raise ZeroDivisionException('!cannot be divided by zero!')
    
    print(users_numbers[0] / users_numbers[1])

except ZeroDivisionException as error:
    print(error)

print('Script isn\'t stopped')
