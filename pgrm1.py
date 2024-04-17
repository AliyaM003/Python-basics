print("Hello function")
def solveit2():
      print("This is line 123")
      print("I am not getting PRINTED")
def solveit4():
      print("Iam solveit4")
      print("This is getting executed")
      solveit2()
      print("second line is getting executed")
def solveit():
        print("This is line 111")
        print("This is line 112")
        solveit4()
        print("solveit4 have not completed its execution")
def sumofTwonumbers(num1,num2):
    print("After execution")
    solveit()
    result("Nothing gets printed")
    result=num1+num2
    print("Before execution")
    return result
    print("last line is getting printed")
num1=int(input())
num2=int(input())
result=sumofTwonumbers(num1,num2)
print(result)
print("first line is getting executed")

