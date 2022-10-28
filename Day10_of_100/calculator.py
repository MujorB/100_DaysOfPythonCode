#! /usr/bin/python3

# Calculator

import cal_art

print(cal_art.logo)
# addition
def addt(a, b):
    """
    Returns the sum of "a" and "b".
    """
    return a + b

# subtraction
def subt(a, b):
    """
    Returns the subtraction of "a" and "b".
    """
    return a - b

# multiplication
def mult(a, b):
    """
    Returns the product of "a" and "b".
    """
    return a * b

# divide
def divs(a, b):
    """
    Returns the division of "a" and "b".
    """
    return a / b


operations = {
    "+": addt,
    "-": subt,
    "*": mult,
    "/": divs,
}

"""
for symbol in operations:
    if symbol == pick_ops:
        answer = addt(num_1, num_2)
        break
    elif symbol == pick_ops:
        answer = subt(num_1, num_2)
        break
    elif symbol == pick_ops:
        answer = mult(num_1, num_2)
        break
    elif symbol == pick_ops:
        answer = divs(num_1, num_2)
        break
    """
# Easier method

continue_cal = False
answer = 0

def calculator():
    num_1 = float(input("What is the first number? "))
    for ops in operations:
        print(ops)

    while not continue_cal:
        pick_ops = input("Pick an operation: ")
        calculator_functions = operations[pick_ops]
        num_2 = float(input("What is the next number? "))

        answer = calculator_functions(num_1, num_2)

        print(f"{num_1} {pick_ops} {num_2} = {answer}")
        num_1 = answer
        check = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to begin calculations again: ")
        if check == 'n':
            calculator()

calculator()
