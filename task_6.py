a = float(input('distance for the first day: '))
b = float(input('final distance: '))
day = 1

while a < b:
    diferant_of_distance = (a / 100) * 10
    a += diferant_of_distance
    day += 1

print(f'in {day} days')
