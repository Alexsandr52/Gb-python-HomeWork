# user_list = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
user_list = list(map(int, input('Enter a sequence of numbers separated by a space: ').strip().split()))
result = [el for el in user_list if el not in user_list[user_list.index(el) + 1:]]
print(result)
