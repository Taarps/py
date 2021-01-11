# calculator
from art import logo

#add
def add(n1, n2):
    return n1 + n2

#subtract
def subtract(n1, n2):
    return n1 - n2

#multiply
def multiply(n1, n2):
    return n1 * n2

#divide
def divide(n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

def calculator():
    print(logo)

    num1 = float(input("What the first number?: "))
    for symbol in operations:
        print(symbol)
    repeat = True

    while repeat:
        operation_symbol = input("Pick an operation: ")
        num2 = float(input("What the next number?: "))
        calculation_function = operations[operation_symbol]
        answer = calculation_function(num1, num2)

        print(f"{num1} {operation_symbol} {num2} = {answer}")

        if input(f"Type 'y' to countinue calculating with {answer}, or type 'n' to start new calculation: ") == "y":
            num1 = answer
        else:
            repeat = False
            calculator()

calculator()