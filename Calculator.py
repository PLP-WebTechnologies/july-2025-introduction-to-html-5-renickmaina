# Prompts user to enter first number
num1 = float(input("Enter the first number: "))

# Prompts user to enter second number
num2 = float(input("Enter the second number: "))

# Ask the user for the operation
operation = input("Enter the operation (+, -, *, /): ")

# Calculations
if operation == "+":
    result = num1 + num2
    print(f"{num1} + {num2} = {result}")
elif operation == "-":
    result = num1 - num2
    print(f"{num1} - {num2} = {result}")
elif operation == "*":
    result = num1 * num2
    print(f"{num1} * {num2} = {result}")
elif operation == "/":
    if num2 != 0:
        result = num1 / num2
        print(f"{num1} / {num2} = {result}")
    else:
        print("Error: Division by zero is not allowed.")
else:
    print("Invalid operation! Please enter +, -, * or /.")
