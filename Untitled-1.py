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