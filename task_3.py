class Cell:
    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        return Cell(self.value + other.value)
    
    def __sub__(self, other):
        new_cell = self.value - other.value
        if new_cell >= 0:
            return Cell(new_cell)
        else:
            print('something wrong')
            return None

    def __mul__(self, other):
        return Cell(self.value * other.value)

    def __truediv__(self, other):
        return Cell(self.value // other.value)
    
    def make_order(self, count):
        s = ''
        for i in range(self.value // count):
            s += '*' * count + '\n'
        s += '*' * (self.value % count) + '\n'
        return s

    def __str__(self):
        return str(self.value)

cell = Cell(41)
print(cell.make_order(3))
cell_2 = Cell(56)
print(cell_2.make_order(6))

print(cell_2 - cell)
print(cell_2 + cell)
print(cell_2 / cell)
print(cell - cell_2)
