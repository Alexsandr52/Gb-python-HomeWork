def my_func(x, y):
    if y > 0:
        return 'y must be less than 0'
    elif x < 0:
        return 'x must be greater than 0'

    return x**y

user_x = float(input('Enter x: '))
user_y = int(input('Enter y: '))

print (my_func(user_x, user_y))
