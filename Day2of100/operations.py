#!/usr/bin/python3

# Addition
print(1 + 2)

# Subtraction
print(10 - 5)

# Multiplication
print(2 * 2)

# Division, division in python always result to a float
print(type(10 / 3))

# To avoid a floating point result the float divission can be utilized
print(10 // 3)
print(type(10 // 3))

# Exponent i.e power of
print(2 ** 2)

"""
Order of priority, remember the math formular PEMDAS same applies in python
()
**
*/
+-
"""

"""
# The round() function in python is used to round a floating point numbers to its
nearest whole numbers as the int() functions truncates the values after the floating
points. The round() functions can be control the precision of a value by add following the value with the precision value to be achieved
"""
# E.g
value = 8 / 3
print(value)

round_func = round(value)
print(round_func)

precision = round(value, 2)
print(precision)

