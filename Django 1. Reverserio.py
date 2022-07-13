class Car:

    wheels_number = 4

    def __init__(self, name='_', color='_', year=2020, is_crashed=True):
        self.name = name
        self.color = color
        self.year = year
        self.is_crashed = is_crashed


bmw_car = Car(name='BMW x5', color='Blue')
mazda_car = Car(name='mazda X67', year=1999, is_crashed=False)

print(bmw_car.year, mazda_car.year, bmw_car.is_crashed, mazda_car.wheels_number, sep='\n')

how_many_wheels_have_5_cars = Car.wheels_number * 5
print(f'5 cars have {how_many_wheels_have_5_cars} wheels')