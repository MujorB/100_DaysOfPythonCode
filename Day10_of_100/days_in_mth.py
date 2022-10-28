#! /usr/bin/python3

def is_leap(year):
    if year % 4 == 0:
        result = True
    elif year % 100 == 0:
        result = False
    elif year % 400 == 0:
        result = True
    else:
        result = False
    return result

def days_in_month(year, month):
    """
    Takes any particular year and month in numbers and returns the numbers of days in that month taking into consideration the leap year.
    """
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]  
    if is_leap(year):
        if month == 2:
            return month_days[month - 1] + 1
        return month_days[month - 1]
    else:
        return month_days[month - 1]


#🚨 Do NOT change any of the code below 
year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(days)
