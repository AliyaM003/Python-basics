print("starting line")
try:
    a=10/5
except:
    print("some exception raised")
else:
    print("no exception raised,everything worked perfectly")
finally:
    print("this is a final block")
    print("outside try block")    
