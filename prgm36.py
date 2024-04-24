class car:
    def __init__(self,speed):
          self.speed = speed
          self.brand= "audi"
          self.wheelscount = 4

car1 = car(110)
print(car1.speed)
car2 = car(70)
print(car1.speed)
car3 = car(85)
print(car2.speed)
print(car1.brand)
car2.brand = "toyota"
print(car1.brand)
car3.brand = "honda-city"
print(car2.brand)
print(car1.wheelscount)
print(car3.brand)
car3.spped = 30
car2.wheelscount = 10
print(car3.speed)
