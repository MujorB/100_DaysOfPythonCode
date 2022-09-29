#! /usr/bin/python3

import random

# 🚨 Don't change the code below 👇
test_seed = int(input("Create a seed number: "))
random.seed(test_seed)

# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
list_num = len(names) - 1

random_name = random.randint(0, list_num)
you_my_friend = names[random_name]
print(f"{you_my_friend} is going to buy the meal today!")