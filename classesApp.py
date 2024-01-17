
class Car:
    def __init__(self,year, make, model):
        self.year = year
        self.make = make
        self.model = model
    def age(self):
        Car.age = 2024 - self.year
        print(f'The car age is {Car.age}')

toyota1 = Car(1984,"Toyota","Celica" )       

print(toyota1.year)
toyota1.age()


