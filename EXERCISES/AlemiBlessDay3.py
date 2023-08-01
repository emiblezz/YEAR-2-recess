def calculate():
    try:
        num1 = float(input("Enter number 1: "))
        num2 = float(input("Enter number 2: "))
        operator = input("Enter operator (+, -, *, /): ")

        if operator == '+':
            result = num1 + num2
        elif operator == '-':
            result = num1 - num2
        elif operator == '*':
            result = num1 * num2
        elif operator == '/':
            result = num1 / num2
        else:
            result = "Invalid operator"

        print("Result:", result)

    except (ValueError, ZeroDivisionError):
        print("Error: Invalid input")

# Main program
print("ALEMI BLESS Simple Calculator")

# Perform calculation
calculate()
