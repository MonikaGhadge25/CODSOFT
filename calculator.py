# Task - 2 Simple calculator
def calculator():
    print("-------------------------------------------")
    print("-----Welcome to the Simple Calculator!-----")
    print("-------------------------------------------")
    print("Operations:")
    print("+ for Addition")
    print("- for Subtraction")
    print("* for Multiplication")
    print("/ for Division")
    
    print("")
    num1 = float(input("Enter the First Number: "))
    num2 = float(input("Enter the Second Number: "))
    operation = input("Enter the Operation (+, -, *, /): ")

    if operation == '+':
        result = num1 + num2
        print(f"\nThe Result of {num1} + {num2} is: {result}\n")
    elif operation == '-':
        result = num1 - num2
        print(f"\nThe Result of {num1} - {num2} is: {result}\n")
    elif operation == '*':
        result = num1 * num2
        print(f"\nThe Result of {num1} * {num2} is: {result}\n")
    elif operation == '/':
        if num2 != 0:
            result = num1 / num2
            print(f"\nThe Result of {num1} / {num2} is: {result}\n")
        else:
            print("Error: Division by zero is not allowed.\n")
    else:
        print("Invalid Operation Selected.\n")

calculator()
