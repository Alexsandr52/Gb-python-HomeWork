import time

class TrafficLight:
    def __init__(self, color):
        self._color = color
    
    def running(self):
        light_data = ['green', 'yellow', 'red', 'yellow']
        light_time = [5, 2, 7, 2]
        index = light_data.index(self._color)
        while True:
            print(light_data[index])
            time.sleep(light_time[index])
            index += 1
            if index == len(light_data):
                index = 0

traffic_light = TrafficLight('red')
traffic_light.running()
