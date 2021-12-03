products = []
index = 1
user_input = ''
while user_input != 'stop':
    name = input('Enter name of prod: ')
    prise = input('Enter prise: ')
    quantity = input('Enter the quantity: ')
    units = input('Enter the unit: ')

    products.append(
        (index, { 'name': name, 'prise': prise, 'quantity': quantity, 'units': units})
    )
    
    index += 1
    user_input = input('Enter \'stop\' to continue: ')

print(products)

products_dict = {}

for indx, lokal_dict in products:
    for key, value in lokal_dict.items():
        if not products_dict.get(key):
            products_dict[key] = [value]
        else:
            products_dict[key].append(value)

for key, value in products_dict.items():
    products_dict[key] = list(set(value))

print(f'\n full products dict {products_dict}')
