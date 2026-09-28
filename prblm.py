class Car:
    def __init__(self,brand):
        self.brand = brand
    def display(self):
        print("I have a car.it is of brand:",self.brand)
class BMW(Car):
    def __init__(self):
      super().__init__("BMW")
class Audi(Car):
    def __init__(self):
      super().__init__("Audi")



            
