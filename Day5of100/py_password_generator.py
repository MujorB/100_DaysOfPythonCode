#! /usr/bin/python3

import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91

all_letters = len(letters)
all_symbols = len(symbols)
all_numbers = len(numbers)

ltrs_pswd = ""
symbl_pswd = ""
nmbrs_pswd = ""

for ltrs in range(0, nr_letters):
    rand_ltrs = random.randint(0, all_letters - 1)
    ltrs_pswd += letters[rand_ltrs]

for symbls in range(0, nr_symbols):
    rand_symbl = random.randint(0, all_symbols - 1)
    symbl_pswd += symbols[rand_symbl]

for nmbrs in range(0, nr_numbers):
    rand_nmbrs = random.randint(0, all_numbers - 1)
    nmbrs_pswd += numbers[rand_nmbrs]

all_psswd = ltrs_pswd + symbl_pswd + nmbrs_pswd
print(all_psswd)


#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

randomized_psswd = ''.join(random.sample(all_psswd, len(all_psswd)))
print(randomized_psswd)







"""
#######   IGNORE   ###########

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P 

all_pswd = ltrs_pswd + symbl_pswd + nmbrs_pswd
len_allpswd = len(all_pswd)
list_allstrings_in_all_pswd = []


for all_strings in all_pswd:
    list_allstrings_in_all_pswd += all_strings
    
print(list_allstrings_in_all_pswd)
randomized_number = random.randint(0, len_allpswd - 1)


list_of_pswd_len_random_nmbrs = []
for rand_lst in range(0, len_allpswd):
    list_of_pswd_len_random_nmbrs += str(random.randint(0, len_allpswd - 1))

print(list_of_pswd_len_random_nmbrs)


for i in range(0, len_allpswd):
    any_rand = random.randint(0, len_allpswd - 1)
    if list_of_pswd_len_random_nmbrs[i] ==  list_of_pswd_len_random_nmbrs[-i]:
        if any_rand > int(list_of_pswd_len_random_nmbrs[i]):
            list_of_pswd_len_random_nmbrs[i] = any_rand - int(list_of_pswd_len_random_nmbrs[i])
        else:
            list_of_pswd_len_random_nmbrs[i] = int(list_of_pswd_len_random_nmbrs[i]) - any_rand
        # if list_of_pswd_len_random_nmbrs[i] < 0:
        list_of_pswd_len_random_nmbrs[i] = str(list_of_pswd_len_random_nmbrs[i])
        # print(i)
        i = 0
    print(i)

print(list_of_pswd_len_random_nmbrs)

"""