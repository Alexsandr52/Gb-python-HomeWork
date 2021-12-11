from functools import reduce
main_list = [el for el in range(100, 1001) if not el % 2]
print(reduce(lambda main_el, next_el: main_el * next_el, main_list))