user_string = input('Enter words or a sentence: ').split()

for index, value in enumerate(user_string, 1):
    print(f'{index}) {value[:10]}')
