#! /usr/bin/env python3
"""
################### Scopes ####################
"""

# enemies = 1

# def increase_enemies():
#   enemies = 2
#   print(f"enemies inside function: {enemies}")

# increase_enemies()
# print(f"enemies outside function: {enemies}")


"""
# Local Scope, are variable that could only be accessed within a function e.g
"""
# def drink_portion():
#     portion_strength = 2
#     print(portion_strength)


# drink_portion()
# print(portion_strength)

"""
# Global Scope, are variable available within a function no matter how nested
# and also outside functions.
"""
# player_health = 10

# def drink_portion():
#     portion_strength = 2
#     print(player_health)

# drink_portion()
# print(player_health) 
"""
# Modifing Global Variable
"""
# enemies = "Skeleton"
# print(f"enemies outside function before modification: {enemies}")
# def increase_enemies():
#     # print(f"enemies inside function before modification: {enemies}")
#     global enemies
#     enemies += " Zombies"
#     print(f"enemies inside function: {enemies}")


# increase_enemies()
# print(f"enemies outside function: {enemies}")

"""
Global constant, should in case you want to use a variable which you intend 
not to modify(CONSTANT) at all in the course of the program, the you could use
the UPPER_CASE variable representation method to remind yourself as to not touch
such variable .e.g.
"""
PI = 3.14159
URL = "https://www.goggle.com"
TWITTER_HANDLE = "@mujorb_01"
EMAIL = "mujorb@gmail.com"
