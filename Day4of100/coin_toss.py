#! /usr/bin/python3

import random
#Remember to use the random module
#Hint: Remember to import the random module here at the top of the file. 🎲
	 
# 🚨 Don't change the code below 👇
test_seed = int(input("Create a seed number: "))
random.seed(test_seed)
 # 🚨 Don't change the code above 👆 It's only for testing your code.
	 
#Write the rest of your code below this line 👇
zero_or_one = random.randint(0, 1)

print(zero_or_one)
if zero_or_one:
    print("Heads")
else:
    print("Tails")
