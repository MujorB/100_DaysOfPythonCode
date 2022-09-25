#! /usr/bin/python3

"""
----------------------- A Body Mass Index Calculator ---------------------

"""

# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

bmi = round(weight / height ** 2)
result = ""
undr_wght = "are underweight."
over_wght = "are slightly overweight."
norm_wght = "have a normal weight."
obes_     = "are obese."
clin_obes = "are clinically obese."

if bmi < 18.5:
    result = undr_wght
elif bmi < 25:
    result = norm_wght
elif bmi < 30:
    result = over_wght
elif bmi < 35:
    result = obes_
else:
    result = clin_obes

print(f"Your BMI is {bmi}, you {result}.")