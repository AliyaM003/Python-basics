
class bike:
    def __init__(self,speed,brand,wheelscount):
          self.speed = speed
          self.brand = brand
          self.wheelscount = 12
    def printwheels(self):
        print("wheels count is:",self.wheelscount)
    def printbrand(self):
        print("brandname is:",self.brand)
    def printspeed(self):
        print("sorry i am not going to print speed ")

bike1 = bike(90,"R-1 5", 2)
bike2 = bike(115,"GT", 2)
bike3 = bike(65,"pulsar", 4)
print(bike2.printbrand())
bike2.printbrand()
bike3.printspeed()
bike1.printwheels()
bike1.printbrand()
bike3.printbrand()
        

