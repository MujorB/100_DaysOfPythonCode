#! /usr/bin/python3

# Python loops
fruits = ['Apple', 'Pears', 'Cherry']

for fruit in fruits:
    print(fruit)
    print(fruit + '-Pie')

# For loops with range.
"""
The range function steps through the number specified in its agument one by one and not includding the very last number, for it to step throught more than once another int paramater can be added. e.g.
range(1, 10, 2)
"""
for steps in range(0, 10, 2):
    print(steps)


# A program that add all numbers from 1 to 100.
total = 0
for numbers in range(1, 101):
    total += numbers
print(total)