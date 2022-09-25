#! /usr/bin/python3

#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇

print("Welcome to the tip calculator.")
total_bill = float(input("What was the total bill? $"))
tip_percent = float(input("What percentage tip would you like to give? 10, 12, or 15? "))
bill_split = float(input("How many people to split the bill? "))

tip_percent = (tip_percent / 100) * total_bill
tip_n_bills = tip_percent + total_bill

each_paye = (tip_n_bills / bill_split)
# each_paye = round(each_paye, 2)

print(f"Each person should pay: ${each_paye:.2f}")

