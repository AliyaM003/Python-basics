#import calculator
#from calculator import add
from calculator import*

print(add(2,3))
print(subtract(4,6))
print(multiply(2,3))
 
def add(a,b):
   return a+b

def subtract(a,b):
   return a-b

def multiply(a,b):
   return a*b

def divide(a,b):
return a//b
