class OrgEquipment():

    def __init__(self, equipment_dict=None):
        if not equipment_dict:
            equipment_dict = {}
        self.equipment_dict = equipment_dict

    def add_org_equipment(self, org_equipment):
        if org_equipment.type not in self.equipment_dict:
            self.equipment_dict.update({org_equipment.type:[org_equipment]})
        else: 
            self.equipment_dict[org_equipment.type].append(org_equipment)
        return True

    def remove_org_equipment(self, org_equipment):
        if org_equipment.type not in self.equipment_dict or len(self.equipment_dict[org_equipment.type]) == 0:
            print(f'{org_equipment.type} not found')
            return False
        else: 
            return self.equipment_dict[org_equipment.type].pop()

class Equipment():

    def __init__(self, type, name, color):
        self.type = type
        self.name = name
        self.color = color

    def __str__(self):
        return f'{self.type}, {self.name}'

class Printer(Equipment):

    def __init__(self, type, name, color, print_type):
        super().__init__(type, name, color)
        self.print_type = print_type
    
class Scanner(Equipment):

    def __init__(self, type, name, color, scan_type):
        super().__init__(type, name, color)
        self.scan_type = scan_type

class Xerox(Equipment):

    def __init__(self, type, name, color, equipment):
        super().__init__(type, name, color)
        self.equipment = equipment

class User():
    def __init__(self, username, admin=False, user_dict=None):
        if not user_dict:
            user_dict = {}
        self.username = username
        self.admin = admin
        self.user_dict = user_dict
    
    @staticmethod
    def take(org_equipment, count, administrator, user):
        administrator.give_away(org_equipment, count,user)

    @staticmethod
    def give_away(org_equipment, count, administrator, user):
        administrator.take(org_equipment, count, user)

class Administrator(User):
    def __init__(self, username, warehouse, admin=False, user_dict=None):
        super(Administrator, self).__init__
        self.admin = True
        self.warehouse = warehouse

    def take(self, org_equipment, count, user):
        for num in range(count):
            if len(user.user_dict[org_equipment.type]) > 0:
                equipment = user.user_dict[org_equipment.type].pop()
                self.warehouse.add_org_equipment(equipment)

    def give_away(self, org_equipment, count, user):
        for num in range(count):
            if len(self.warehouse.equipment_dict[org_equipment.type]) != 0:
                equipment = self.warehouse.remove_org_equipment(org_equipment)
                if org_equipment.type not in user.user_dict:
                    user.user_dict.update({org_equipment.type: [equipment]})
                elif len(user.user_dict[org_equipment.type]) <= 20:
                    user.user_dict[org_equipment.type].append(equipment)
        else:
            return f'sothing wrong'


xerox = Xerox('xerox', 'lg', 'green', 'full')
scanner = Scanner('scanner', 'xiaomi', 'white', 'full')
printer = Printer('printer', 'dexp', 'orange', 'full')

techno_database = {
    'xerox': [xerox, xerox, xerox, xerox, xerox, xerox, xerox],
    'scanner': [scanner, scanner, scanner, scanner, scanner, scanner],
    'printer': [printer, printer, printer, printer, printer, printer, printer]
}

org_equipment = OrgEquipment(techno_database)

admin = Administrator('Alexander', org_equipment)

print('''
a program dedicated to the warehouse of office equipment. 
You can receive and give away equipment to the warehouse. 
<you can take no more than 20 units of a certain vehicle.>
Printer - 0
Scanner - 1
Xerox - 2
''')
teh = [printer, scanner, xerox]

user_input = input('Enter your username: ')
user = User('user_input')

while user_input != 'N':
    user_input = input('take - 1, give away - 2: ')
    if int(user_input) == 1:
        user_input = int(input('''
        Printer - 0
        Scanner - 1
        Xerox - 2 
        :'''))
        count = int(input('Enter count of items: '))
        user.take(teh[user_input], count, admin, user)
    elif int(user_input) == 2:
        user_input = int(input('''
        Printer - 0
        Scanner - 1
        Xerox - 2'''))
        count = int(input('Enter count of items: '))
        user.give_away(teh[user_input], count, admin, user)
    else:
        print('something wrong')

    print(user.user_dict)
    # print(org_equipment.equipment_dict)
    user_input = input('again Y/N: ')
    