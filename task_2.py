class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width
    
    def weight(self, thickness,reference_weight):
        result = self._length * self._width * thickness * reference_weight / 1000
        return result

my_road = Road(20,5000)
print(f'{my_road.weight(5, 25)} т')
