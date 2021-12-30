from abc import ABC, abstractmethod 

class Clothes(ABC):
    def __init__(self, name):
        self.name = name
    
    @abstractmethod
    def fabric_calculation():
        pass

    def sum_fabric_calculation(self, clothes_list):
        final_sum = 0
        for element in clothes_list:
            final_sum += element.fabric_calculation
        return final_sum

class Coat(Clothes):
    def __init__(self, name, V):
        super().__init__(name)
        self.V = V
    
    @property
    def fabric_calculation(self):
        return self.V / 6.5 + 0.5

class Costume(Clothes):
    def __init__(self, name, H):
        super().__init__(name)
        self.H = H

    @property
    def fabric_calculation(self):
        return 2 * self.H + 0.3

coat = Coat('mans', 100)
cost = Costume('versachi', 1.70)
cost_1 = Costume('versachi', 1.50)
cost_2 = Costume('versachi', 1.67)
cost_3 = Costume('versachi', 1.90)

print(coat.fabric_calculation)
print(cost.fabric_calculation)
print(cost.sum_fabric_calculation([cost ,cost_1, cost_2, cost_3]))