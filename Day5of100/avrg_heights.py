#! /usr/bin/python3


all_heights = 0
# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


#Write your code below this row 👇

  all_heights += student_heights[n]

avrg_heights = round(all_heights / (n + 1))
print(avrg_heights)