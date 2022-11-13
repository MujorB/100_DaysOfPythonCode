#! /usr/bin/env python3
"""
Program:    Higher vs Lower game.
Author:     Bright Mujor <mujorb@gmail.com>
Course:     100 days of python code by Angella Yu <day 14>
Date:       Fri 08-11-2022.
Bug Fix:    Duration: <6 days>; Date Fixed: <Sun 13-11-2022>.
"""

import random
import game_art, game_data


def main():
    ALL_DATA = (len(game_data.data) - 1)

    first_rand_data = random.randint(0, ALL_DATA)
    compare_data_01 = first_rand_data

    global player_score
    player_score = 0

    compare_data_02 = compare_data_01 + 1
    if compare_data_02 < ALL_DATA:
        compare_data_02 %= ALL_DATA

    def check_ans():
        if followers_data_01 > followers_data_02:
            result = "A"
        else:
            result = "B"
        return result

    def check_input():
        player_input = "Test Char"
        while player_input not in "AB":
            player_input = input("Who has more followers? Type 'A' or 'B': ")
            if player_input == "A" or player_input == "B":
                continue
            else:
                print("Please type 'A' or 'B' ")
        return player_input

    def compare_ans():
        player_input02 = check_input()
        if player_input02 == check_ans():
            global player_score
            player_score += 1
            result = f"You're right! Current score: {player_score}."
        else:
            result = f"\n\nSorry, that's wrong. Final score: {player_score}"
        return result

    def game_body():
        global followers_data_01
        global followers_data_02

        name_data_01 = game_data.data[compare_data_01]["name"]
        descriptn_data_01 = game_data.data[compare_data_01]["description"]
        country_data_01 = game_data.data[compare_data_01]["country"]
        followers_data_01 = game_data.data[compare_data_01]["follower_count"]

        name_data_02 = game_data.data[compare_data_02]["name"]
        descriptn_data_02 = game_data.data[compare_data_02]["description"]
        country_data_02 = game_data.data[compare_data_02]["country"]
        followers_data_02 = game_data.data[compare_data_02]["follower_count"]


        compare_A = f"{name_data_01}, a {descriptn_data_01}, from {country_data_01}."
        against_B = f" {name_data_02}, a {descriptn_data_02}, from {country_data_02}."

        print(game_art.logo)
        print(f"Compare A: {compare_A}")
        print(game_art.vs)
        print(f"Against B:{against_B} ")

        compare_result = compare_ans()
        if "Sorry" not in compare_result:
            print("\n" * 30, compare_result)
            game_progress = player_score
        else:
            game_progress = 0
            print(compare_result)
        return game_progress

    play_game = True
    while play_game:
        continue_game_body = game_body()
        compare_data_01 = compare_data_02

        compare_data_02 = random.randint(0, ALL_DATA)
        if compare_data_02 <= ALL_DATA:
            compare_data_02 %= ALL_DATA
        if continue_game_body == 0:
            break

if __name__ == "__main__":
    main()
