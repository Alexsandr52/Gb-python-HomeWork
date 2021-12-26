class Worker:
    def __init__(self,  name, surename, position, salary, prize):
        self.name = name
        self.surename = surename
        self.position = position
        self._incom = {'salary': salary, 'prize': prize}

class Position(Worker):
    def get_full_name(self):
        full_name = f'{self.name} {self.surename}'
        return full_name
    
    def get_total_income(self):
        total_income = f'{self._incom["salary"] + self._incom["prize"]} р'
        return total_income

jun = Position('Ivan','Khonyavin','jun', 1000,  500)
print(jun.get_full_name())
print(jun.get_total_income())

mid = Position('Vladislav','Botchkarew','mid',10000, 700)
print(mid.get_full_name())
print(mid.get_total_income())

jun = Position('Oleg','Virodov','jun',1500, 700)
print(jun.get_full_name())
print(jun.get_total_income())
#доработать словарь
