from abc import ABC,abstractmethod

class Box(ABC):
    @abstractmethod
def printPrice(self):
    pass

@abstractmethod
def printColour(self):
    pass

Class Box2(Box):
   def printPrice(self):
print("Price is 45k")
