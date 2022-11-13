#! /usr/bin/env python3

import random

ALL_DATA = (len(data) - 1)
# print(game_art.logo)
# print(ALL_DATA)

def check_ans():
    if followers_data_01 > followers_data_02:
        print(f"followers_count data one >>> {followers_data_01}")
        result = "A"
    else:
        result = "B"
        print(f"followers_count data Two >>> {followers_data_02}")
    print(f"result is >>> {result}")
    return result

def compare_ans():
    def check_input():
        player_input = input("Who has more followers? Type 'A' or 'B': ")
        if player_input == "A" or player_input == "B":
            print(player_input)
        else:
            print("Please type 'A' or 'B' ")
            check_input()
        return player_input

    player_input02 = check_input()
    print(f"player input >>> {player_input02}")
    if player_input02 == check_ans():
        result = "Wow!! you're correct :)"
    else:
        result = "Ooops!! you're wrong :("
    return result



first_rand_data = random.randint(0, ALL_DATA)
compare_data_01 = first_rand_data
# please note the value of compare_data_02 not to exceed ALL_DATA  
compare_data_02 = compare_data_01 + 1
# print(data[compare_data_01])
name_data_01 = data[compare_data_01]["name"]
descriptn_data_01 = data[compare_data_01]["description"]
country_data_01 = data[compare_data_01]["country"]
followers_data_01 = data[compare_data_01]["follower_count"]

name_data_02 = data[compare_data_02]["name"]
descriptn_data_02 = data[compare_data_02]["description"]
country_data_02 = data[compare_data_02]["country"]
followers_data_02 = data[compare_data_02]["follower_count"]


print(f"Compare A: {name_data_01}, a {descriptn_data_01}, from {country_data_01}. == {followers_data_01} ")
print(game_art.vs)
print(f"Against B: {name_data_02}, a {descriptn_data_02}, from {country_data_02}. ==  {followers_data_02} ")


print(compare_ans())