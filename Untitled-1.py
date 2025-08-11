def add(a, b):
    answer = a + b
    print (a , " + " , b , " = " , answer)

def subtract(a, b):
    answer = a - b
    print (a , " - " , b , " = " , answer)

def multiply(a, b):
    answer = a * b
    print (a , " * " , b , " = " , answer)

def divide(a, b):
    if b == 0:
        print("Division by zero is not allowed.")
    else:
        answer = a / b
        print (a , " / " , b , " = " , answer)

while True:
    print("\n")
    print("Calculator!")
    print("A. Add")
    print("B. Subtract")
    print("C. Multiply")
    print("D. Divide")
    print("E. Exit")

    choice= input("Enter your choice (A-E): ")
    print("\n")
    if choice == 'A' or choice == 'a':
        print("You chose addition")
        a = int(input("Enter the first number: "))
        b = int(input("Enter the second number: "))
        add(a, b)
    elif choice == 'B' or choice == 'b':
        print("You chose subtraction")
        a = int(input("Enter the first number: "))
        b = int(input("Enter the second number: "))
        subtract(a, b) 
    elif choice == 'C' or choice == 'c':
        print("You chose multiplication")
        a = int(input("Enter the first number: "))
        b = int(input("Enter the second number: "))
        multiply(a, b)
    elif choice == 'D' or choice == 'd':
        print("You chose division")
        a = int(input("Enter the first number: "))
        b = int(input("Enter the second number: "))
        divide(a, b)
    elif choice == 'E' or choice == 'e':
        print("Exiting the calculator. Goodbye!")
        quit()
    else:
        print("Invalid choice. Choose between A-E.")