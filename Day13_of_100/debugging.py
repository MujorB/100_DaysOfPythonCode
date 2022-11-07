#! /usr/bin/env python3
############DEBUGGING#####################

# # Describe Problem
# def my_function():
#   for i in range(1, 20):
#     if i == 20:
#       print("You got it")
# my_function()

"""
Function does not print statement cause the range function
never gets to 20.
"""
# def my_function():
#     """Fix"""
#     for i in range(1, 21):
#         if i == 20:
#           print("You got it")
# my_function()  #checked
# ==========================================================


# # Reproduce the Bug
# from random import randint
# dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]
# dice_num = randint(1, 6)
# print(dice_imgs[dice_num])

"""
Error: as a result of index out of range **fixed**
# Reproduce the Bug [Fix]
from random import randint
dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]
dice_num = randint(0, 5)
print(dice_imgs[dice_num])
"""
# ====================================================================


# # Play Computer
# year = int(input("What's your year of birth?"))
# if year > 1980 and year < 1994:
#   print("You are a millenial.")
# elif year > 1994:
#   print("You are a Gen Z.")


"""# Error fixed : The year 1994 does not print any statement.
# Play Computer
year = int(input("What's your year of birth? "))
if year >= 1980 and year <= 1994:
  print("You are a millenial.")
elif year > 1994:
  print("You are a Gen Z.")"""
# =========================================================================== 

# # Fix the Errors
# age = input("How old are you?")
# if age > 18:
# print("You can drive at age {age}.")

"""# Fix the Errors
# Datatype err and python f-string formatting
age = int(input("How old are you? "))
if age > 18:
    print(f"You can drive at age {age}.")
"""
# ===========================================================================


# #Print is Your Friend
# pages = 0
# word_per_page = 0
# pages = int(input("Number of pages: "))
# word_per_page == int(input("Number of words per page: "))
# total_words = pages * word_per_page
# print(total_words)

# debugging
#Print is Your Friend
"""pages = 0
word_per_page = 0
pages = int(input("Number of pages: "))
word_per_page = int(input("Number of words per page: "))
total_words = pages * word_per_page
print(total_words)"""
# ==============================================================/


# #Use a Debugger
# def mutate(a_list):
#   b_list = []
#   for item in a_list:
#     new_item = item * 2
#   b_list.append(new_item)
#   print(b_list)

# mutate([1,2,3,5,8,13])

"""
#Use a Debugger
def mutate(a_list):
  b_list = []
  for item in a_list:
    new_item = item * 2
    b_list.append(new_item)
  print(b_list)

mutate([1,2,3,5,8,13])
"""



