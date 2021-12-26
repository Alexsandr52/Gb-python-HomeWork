class Car:
    def __init__(self, speed, color, name, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police
    
    def go(self):
        return 'go'

    def stop(self):
        return 'stop'

    def turn(self, direction):
        return f'turn to {direction}'
    
    def show_speed(self):
        return f'speed is {self.speed}'

class SportCar(Car):
    pass

class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            return 'speed exceeded'

class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            return 'speed exceeded'

class PoliceCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, True)

town_car = TownCar(62, 'green', 'lada')
sport_car = SportCar(262, 'blue', 'supra')
work_car = WorkCar(42, 'red', 'kia')
police_car = PoliceCar(162, 'black', 'lada')

print(town_car.show_speed())
print(work_car.show_speed())
print(town_car.turn('left'))
print(police_car.go())
print(sport_car.turn('right'))
print(police_car.is_police)
print(town_car.name)