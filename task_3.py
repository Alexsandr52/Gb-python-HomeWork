class CheckForNumbers(Exception):

    def __init__(self, text):
        self.text = text

user_str = ''
user_list = []
while(user_str != 'stop'):
    try:
        user_str = input('Enter a number or \'stop\' to stop: ')
        if not user_str.isdigit():
            raise checkForNumbers('srting isn\'t number: ')
        user_list.append(int(user_str))
    except checkForNumbers as error:
        print(error)

print(user_list)
