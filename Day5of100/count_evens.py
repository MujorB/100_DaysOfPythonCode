#! /usr/bin/python3

#Write your code below this row 👇
# A program that add all the even number from and including 1 to 100.

evens_to100 = 0

for evens in range(0, 101, 2):
    evens_to100 += evens
print(evens_to100)