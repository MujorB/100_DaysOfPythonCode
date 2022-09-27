#! /usr/bin/python3

print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height >= 120:
    print("You can ride the rollercoaster!")
    age = int(input("What is your age? "))
    photo = (input("Do you want a photo for your ticket? Yes or No\n"))
    bill = 0

    if photo == "Yes":
        bill += 3
    if age < 12:
        bill += 5
    elif age < 18:
        bill += 7
    elif age >= 45 and age <= 55:
        bill = 0
    else:
        bill += 12
    if bill:
        print(f"Your total bill is ${bill}.")
    else:
        print("Everything is going to be ok. have a free ride on us!")
else:
    print("Sorry, you have to grow taller before you can ride.")