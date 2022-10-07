#!/usr/bin/python3

import random

#Step1

word_list=["aardvark","baboon","camel"]

# TODO-1-Randomlychooseawordfromtheword_listandassignittoavariablecalledchosen_word.
chosen_word = random.choice(word_list)
print(chosen_word)

# TODO-2-Asktheusertoguessaletterandassigntheiranswertoavariablecalledguess.Makeguesslowercase.
guess = input("Guess a letter from our chosen word? ")

# TODO-3-Checkifthelettertheuserguessed(guess)isoneofthelettersinthechosen_word.
for letter in chosen_word:
    i = 0
    if letter == chosen_word[i]:
        print("Right")
    else:
        print("Wrong")