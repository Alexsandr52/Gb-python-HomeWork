original_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]

greater_than_previous = [element for element in original_list if element > original_list[original_list.index(element) - 1] and original_list.index(element) != 0]
print(greater_than_previous)
