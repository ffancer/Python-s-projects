class Car:

    wheels_number = 4

    def __init__(self, name='_', color='_', year=2020, is_crashed=True):
        self.name = name
        self.color = color
        self.year = year
        self.is_crashed = is_crashed

    def drive(self):
        print(f'{self.name.title()} is driving.')

opel_car = Car('opel Astra', 'red', 2016, False)
opel_car.drive()
print(opel_car.color)