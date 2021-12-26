class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print(f'I draw with {self.title}')

class Pen(Stationery):
    def draw(self):
        print('I draw with a pen')

class Pencil(Stationery):
    def draw(self):
        print('I draw with a pencil')

class Handle(Stationery):
    def draw(self):
        print('I draw with a marker')

something = Stationery('some item')
something.draw()

pen = Pen('pen')
pen.draw()

pencil = Pencil('pencil')
pencil.draw()

handle = Handle('handel')
handle.draw()
