
def int_func(word):
    new_word = word[0].upper() + word[1:].lower()
    return new_word

user_input = input('Enter your sentence: ').split()
for word in user_input:
    print(int_func(word), end=' ')
    