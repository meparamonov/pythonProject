class Transport:
    # atribut
    name = 'Mazda'
    count = 0

    def __init__(self, color, year): #konstructor
        self.c = color
        self.y = year

    # metod
    def go(self):
        return f'auto {self.name} poexal'

class Car(Transport):
    pass

class Bus(Transport):
    def route(self):
        return f'ha marshrute'

car1 = Car('red', 2020)
print(car1)
print(car1.go())
print(car1.name)
print(car1.y)

car2 = Bus('red', 2023)
print(car2.go())
print(car2.route())