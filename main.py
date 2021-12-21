import math
def multiplication(a, b):
    return a * b
def division(a, b):
    return a / b
def addition(a, b):
    return a + b
def subtraction(a, b):
    return a * b
def squareroot(a):
    return math.sqrt(a)
def exponent(a, b):
    return a ** b
def sin(a):
    return math.sin(a)
def cos(a):
    return math.cos(a)
def tan(a):
    return math.tan(a)
print("""
\033[1mScientific Calculator \033[0m
Choose a number for the following operations
1 - Addition
2 - Subtraction
3 - Multiplication
4 - Division
5 - Exponent
6 - Squareroot
7 - sin(x)
8 - cos(x)
9 - tan(x)
""")
try:
    operation = int(input("What operation would you like to perform: "))
    while 0 < operation < 10:
        print("Enter Parameters")
        a = float(input("Enter a number: "))
        if operation < 6:
            b = float(input("Enter another number: "))
        if operation == 1:
            print(addition(a, b))
        elif operation == 2:
            print(subtraction(a, b))
        elif operation == 3:
            print(multiplication(a, b))
        elif operation == 4:
            print(division(a, b))
        elif operation == 5:
            print(exponent(a, b))
        elif operation == 6:
            print(squareroot(a))
        elif operation == 7:
            print(sin(a))
        elif operation == 8:
            print(cos(a))
        else:
            print(tan(a))
        exit()
    else:
        (print("Invalid Input"))
except ValueError:
    print("Invalid Input")