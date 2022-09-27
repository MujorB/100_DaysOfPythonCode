#! /usr/bin/python3

"""
A love score calculator to check for the compatibility between you and your crush :)
"""

# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

all_names = name1 + name2
all_names = all_names.lower()

trueNum = all_names.count("t")
trueNum += all_names.count("r")
trueNum += all_names.count("u")
trueNum += all_names.count("e")

loveNum = all_names.count("l")
loveNum += all_names.count("o")
loveNum += all_names.count("v")
loveNum += all_names.count("e")

loveScrs = str(trueNum) + str(loveNum)
loveScrs = int(loveScrs)

if loveScrs < 10 or loveScrs > 90:
    print(f"Your score is {loveScrs}, you go together like coke and mentos.")
elif loveScrs >= 40 and loveScrs <= 50:
    print(f"Your score is {loveScrs}, you are alright together.")
else:
    print(f"Your score is {loveScrs}.")