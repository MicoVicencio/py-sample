def addition():
    x,y = numbers()
    return x+y

def subtraction():
    x,y = numbers()
    return x-y

def multiplication():
    x,y = numbers()
    return x*y

def division():
    try:
      x,y = numbers()
    except ZeroDivisionError:
        print("Invalid Second Number! It should not be zero")
    
    return x/y

def numbers():
    n1 = int(input("Enter first number:"))
    n2 = int(input("Enter second number:"))
    return n1,n2

def spaces():
    for i in range(10):
        print(" ")
def main():
  while True:    
    print("Calculator of Modern World")
    print("This offer basic calculation")
    print("1.Addition")
    print("2.Subtarction")
    print("3.Multiplication")
    print("4.Division")
    
    userInput = int(input("Choose from 1 - 4:"))
    if userInput == 1:
      result = addition()
      print("The Sum of two numbers is" , result)
    elif userInput == 2:
      result = subtraction()
      print("The Difference of two numbers is" , result)
    elif userInput == 3:
     result = multiplication()
     print("The Product of two numbers is" , result)
    elif userInput == 4:
      result = division()
      print("The Quotient of two numbers is" , result)
    else:
        print("Invalid Choice!, Try again!")
        spaces()
        continue
    choice = input("Do you want to try again(y/n)")
    if "n" in choice:
        print("The program will now exit!")
        break
    spaces()
        
    
    
main()