class car:
    def __init__(self,speed,brand,wheelscount,model,price):
          self.speed = speed
          self.brand= "audi"
          self.wheelscount = 12
          self.model = "2024-model"
          self.price = "1 lakhs"
          

car1 = car(100,"verna",4,"2023-model","20-lakhs")
car2 = car(80,"thar",6,"2019-model","15-lakhs")
car3 = car(110,"XUV",7,"2022-model","13-lakhs")

print(car1.wheelscount)
print(car2.wheelscount)
print(car3.brand)
print(car1.speed)
car2.price = "18-lakhs"
print(car2.price)
car3.model = "2022 model"
print(car3.model)
print(car1.price)
print(car2.model)


