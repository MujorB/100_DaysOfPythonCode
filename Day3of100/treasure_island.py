#! /usr/bin/python3

print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇

R, L = "right", "left"
wait = "wait"
red, yellow, blue = "red", "yellow", "blue"
cross_road = input("You're at a crossroad. Where do you want to go? type 'left' or 'right'.\n").lower()

if cross_road == L:
    print("Phew!! You manage to escape the jumanji forest! Welcome to the SUJI Lake")
    lake_island = input("There is an island in the middle of the lake. type 'wait' to wait for a boat or 'swim' to swim across. \n").lower()
    if lake_island == wait:
        print("whoah!! You arrived at the Island unharmed.")
        three_doors = input("There is a house with three doors. One red, one yellow and one blue. which one which one do you choose? type the color name. \n").lower()
        if three_doors == yellow:
            print("You Found The Treasure. Hurray!!")
        elif three_doors == red:
            print("whooosh!!, Burned by fire. Game Over!")
        elif three_doors == blue:
            print("Shrruump!!, Eaten by beast. Game Over!")
        else:
            print("Waank!! Game Over!")
    else:
        print("Grrrr!! You have been attacked by Crocs. Game Over!")
else:
    print("Ha! ha! ha!, You fall into a Hole. Game over!.")
