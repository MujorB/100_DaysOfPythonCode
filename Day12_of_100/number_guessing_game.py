#! /usr/bin/env python3
"""
Program:    Number Guessing Game
Author:     Bright Mujor <mujorb@gmail.com>
Course:     100 days of python code by Angella Yu <day 12>
Date:       Mon 31-10-2022.
"""
import random
import game_art


def main():
    def thinking():
        """
        Purpose: Returns guessed number value to be
                 used by the program.
        """
        num_range = []
        for number in range(1, 101):
            num_range.append(number)
        for _ in range(5):
            global thinks
            thinks = random.randint(5, 30)
            print("thinking", "." * thinks)
        print(". " * thinks, "Done :)")
        return random.choice(num_range)

    def game_difficulty():
        """
        Usage: Returns number of player lives according
            to games difficulty level.
        """
        game_level = input("Choose a difficulty. Type 'easy' or 'hard': ")
        if game_level == "easy":
            countdown = 10
        else:
            countdown = 5
        return countdown

    def end_game():
        """
        Usage:   Provide game program checks to show
                player's game progress.
        R.Value: Returns -1 if player's won or 0 if
                player lose.
        """
        remaining_lives = countdown_scores
        while remaining_lives > 0:
            players_guess = int(input("Make a guess: "))
            print()
            if players_guess == random_guess:
                print(
                    f"Wow!! the actual answer was {random_guess},  You Won :)\n"
                )
                remaining_lives = -1
            else:
                if players_guess < random_guess:
                    remaining_lives -= 1
                    print("Too Low.\nGuess again.\n")
                else:
                    remaining_lives -= 1
                    print("Too High.\nGuess again.\n")
                if remaining_lives != 0:
                    print(
                        f"You have {remaining_lives} attempts remaining to guess the number."
                    )
            if remaining_lives == 0:
                print(
                    "Ooopss.....\nSorry all attempts has been used, You Lose :(\n"
                )
        return False

    def game_checks():
        """"""
        end_game_function = end_game()
        while not end_game_function:
            play_again = input(
                "Would you love to play Number Guessing Game? Type 'y' or 'n': "
            )
            if play_again == "y":
                NUMBER_GUESSING_GAME()
            else:
                end_game_function = True
                print("bye", "." * thinks, "\n" * 2)

    def NUMBER_GUESSING_GAME():
        print(game_art.logo)
        print("Welcome to the Number Guessing Game!")
        print("I am thinking of a number between 1 and 100")

        global random_guess
        random_guess = thinking()
        # print(random_guess)
        global countdown_scores
        countdown_scores = game_difficulty()
        print(
            f"You have {countdown_scores} attempts remaining to guess the number."
        )
        game_checks()

    NUMBER_GUESSING_GAME()


if __name__ == "__main__":
    main()
