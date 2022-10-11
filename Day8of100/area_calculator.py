#! /usr/bin/python3

#Write your code below this line 👇

def paint_calc(height="test_h", width="test_w", cover="coverage"):
    area = height * width
    num_of_can = area / cover
    return round(num_of_can + 0.4)

#Write your code above this line 👆
# Define a function called paint_calc() so that the code below works.   

# 🚨 Don't change the code below 👇
test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)

print(f"You'll need {paint_calc(height=test_h, width=test_w, cover=coverage)} cans of paint.")  
