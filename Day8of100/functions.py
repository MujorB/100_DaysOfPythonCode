#! /usr/bin/python3

# Review: 
# Create a function called greet(). 
# Write 3 print statements inside the function.
# Call the greet() function and run your code.
  
from re import L


def greet():
    print("Hi!!")
    print("You are welcome to this space")
    print("You should introduce yourself")

# greet()

# Fuctions that allows for input:
def greet_with_name(name):
    print(f"Hi! {name}...")
    print("You are welcome to our space.")

# greet_with_name('Bright')

# Functions that allows more than one input.

def greet_with(name, location):
    print(f"We're glad to have you here {name}")
    print(f"How is it like in {location}?")
    
# greet_with('Bright', 'Nigeria')

# In python we have what is called a keyword argument functions and a positional argument 
# functions(implemented above)
# Implementation of a keyword fuction

def greet_with(name="me", location="huawi"):
    print(f"Its glad to have you here {name}")
    print(f"How is {location}")

# greet_with(name='Mercy', location = "SouthAfrica")
greet_with(location="Nigeria", name="Happiness")