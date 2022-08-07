from art import logo


# Calculator Code

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 + n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2

operations = {"+": add, "-": subtract, "*": multiply, "/": divide}

def calculator ():
    print(logo)
    tbc ="y"
    number1 = float(input("Enter the first number: "))

    while tbc.lower() == "y":
        number2 = float(input("Enter the next number: "))

        for ops in operations:
            print(ops)

        op = input("Enter the operations from the information above: ")
        calc_function = operations[op]
        answer = calc_function(number1, number2)
        print(f"{number1} {op} {number2} = {answer}")
        number1 = answer
        tbc = input("Do yo want to continue with the calculation: ")
    continue_calc = input("Do yo want to continue with using the calculator: ")
    if continue_calc.lower() == "y":
         calculator()

calculator()