class Car:
    def __init__(self, name='_', color='_', year='_'):
        self.name = name
        self.color = color
        self.year = year


bmw_car = Car(name='BMW x5', color='Blue')
mazda_car = Car(name='mazda X67', year='1999')

print(bmw_car.year, mazda_car.year, sep='\n')
