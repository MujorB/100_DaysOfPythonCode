#! /usr/bin/python3

import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
 

player_two = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
player_one = random.randint(0, 2)
Rock, Paper, Scissors = 0, 1, 2
rck_ppr_scrs = [rock, paper, scissors]

if player_two < 0 or player_two > 2:
    print("Invalid number, You lose")
else:
    print(rck_ppr_scrs[player_two])
    print(f"Computer choose:\n{player_one}\n{rck_ppr_scrs[player_one]}")

    if player_one == player_two:
        print("Its a Tie!!")
    elif player_one == Rock:
        if player_two == Scissors:
            print("You Lose!!")
        else:
            print("You Won!!")
    elif player_one == Scissors:
        if player_two == Paper:
            print("Your Lose!!")
        else:
            print("You Won!!")
    elif player_one == Paper:
        if player_two == Rock:
            print("You Lose!!")
        else:
            print("You Won!!")