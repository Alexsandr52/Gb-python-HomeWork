# 6. * Реализовать структуру данных «Товары». Она должна представлять собой список кортежей.
# Каждый кортеж хранит информацию об отдельном товаре. 
# В кортеже должно быть два элемента — номер товара и словарь с параметрами (характеристиками товара: название, цена, количество, единица измерения). 
# Структуру нужно сформировать программно, т.е. запрашивать все данные у пользователя.
# Пример готовой структуры:
# [
# (1, {“название”: “компьютер”, “цена”: 20000, “количество”: 5, “eд”: “шт.”}),
# (2, {“название”: “принтер”, “цена”: 6000, “количество”: 2, “eд”: “шт.”}), 
# (3, {“название”: “сканер”, “цена”: 2000, “количество”: 7, “eд”: “шт.”})
# ]
# Необходимо собрать аналитику о товарах. Реализовать словарь, в котором каждый ключ — характеристика товара, например название, а значение — список значений-характеристик, например список названий товаров.
# Пример:
# {
# “название”: [“компьютер”, “принтер”, “сканер”],
# “цена”: [20000, 6000, 2000],
# “количество”: [5, 2, 7],
# “ед”: [“шт.”]
# }
production = []
index = 1
user_input = ''
while user_input != 'stop':
    name = input('Enter name of prod: ')
    prise = input('Enter prise: ')
    quantity = input('Enter the quantity: ')
    units = input('Enter the unit: ')

    production.append(
        (index, { 'name': name, 'prise': prise, 'quantity': quantity, 'units': units})
    )
    
    index += 1
    user_input = input('Enter \'stop\' to continue: ')

print(production)

production_dict = {}

for indx, lokal_dict in production:
    for key, value in lokal_dict.items():
        if not production_dict.get(key):
            production_dict[key] = value
        else:
            production_dict[key].append(value)

print(production_dict)
