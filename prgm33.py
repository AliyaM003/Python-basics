# SIMPLE PROGRM OF RECURRSION
def solveIt(value):
    if value > 10:
        return
        
    print(value)
    solveIt(value +1)
print("after")
solveIt(1)
print("before")        

