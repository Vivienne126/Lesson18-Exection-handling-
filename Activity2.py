try:
    num1,num2=eval(input("Enter 2 number seperated by a comma"))
    result=num1/num2
    print("The result is" , result)
except ZeroDivisionError:
    print("Division by zero is error")
except SyntaxError:
    print("Comma is missing")
except:
    print("Wrong input")
else:
    print("No exections")
finally:
    print("This will be executed no matter what")