def addition():
    x, y = numbers()
    return x + y

def subtraction():
    x, y = numbers()
    return x - y

def multiplication():
    x, y = numbers()
    return x * y

def division():
    try:
        x, y = numbers()
        if y == 0:
            raise ZeroDivisionError("Invalid Second Number! It should not be zero")
        return x / y
    except ZeroDivisionError as e:
        print(e)

def numbers():
    try:
        n1 = int(input("Enter first number: "))
        n2 = int(input("Enter second number: "))
        return n1, n2
    except ValueError:
        print("Invalid input! Please enter a valid integer.")

def spaces():
    for i in range(10):
        print(" ")

while True:    
    print("Calculator of Modern World")
    print("This offers basic calculations")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    
    try:
        userInput = int(input("Choose from 1 - 4: "))
        if userInput == 1:
            result = addition()
            print("The sum of two numbers is", result)
        elif userInput == 2:
            result = subtraction()
            print("The difference of two numbers is", result)
        elif userInput == 3:
            result = multiplication()
            print("The product of two numbers is", result)
        elif userInput == 4:
            result = division()
            if result is not None:
                print("The quotient of two numbers is", result)
        else:
            print("Invalid choice! Please try again.")
            spaces()
            continue
        
        choice = input("Do you want to try again (y/n): ")
        if choice.lower() != "y":
            print("The program will now exit!")
            break
        spaces()
    except ValueError:
        print("Invalid input! Please enter a valid integer.")
