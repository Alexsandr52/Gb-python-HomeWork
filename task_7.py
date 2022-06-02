class ComplexNumber():
    def __init__(self, complex_number):
        self.complex_number = complex_number

    def __str__(self):
        return f'{self.complex_number[0]} + {self.complex_number[1]}i'

    def __add__(self, other):
        result = [self.complex_number[0] + other.complex_number[0], self.complex_number[1] + other.complex_number[1]]
        return ComplexNumber(result)
    
    def __mul__(self, other):
        result = [self.complex_number[0] * other.complex_number[0] - self.complex_number[1] * other.complex_number[1], self.complex_number[0] * other.complex_number[1] + other.complex_number[0] * self.complex_number[1]]
        return ComplexNumber(result)

my_complex_number = ComplexNumber([8, 2])
my_complex_number2 = ComplexNumber([9, 7])
print(f'z1 = {my_complex_number}')
print(f'z2 = {my_complex_number2}')
print(f'{my_complex_number} + {my_complex_number2} = {my_complex_number + my_complex_number2}')
print(f'{my_complex_number} * {my_complex_number2} = {my_complex_number * my_complex_number2}')

