class Car:
    wheels_number = 4

    def __init__(self, name='_', color='_', year=2020, is_crashed=True):
        self.name = name
        self.color = color
        self.year = year
        self.is_crashed = is_crashed

    def drive(self, city):
        print(f'{self.name.title()} is driving to {city}.')

    def change_color(self, new_color):
        self.color = new_color


opel_car = Car('opel Astra', 'red', 2016, False)
opel_car.drive('Moscow')
opel_car.change_color('purple')
print(opel_car.color)
