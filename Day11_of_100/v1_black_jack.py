#! /usr/bin/python3

"""
Black Jack Game, Day 11 of 100daysOfCode Capstone Project.
"""

import random


cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def draw():
    """
    Draw and returns a random card from the card list without
    removing the card drawn from the list.
    """
    return random.choice(cards)

a, b, c, d, e = draw(), draw(), draw(), draw(), draw()


def add_cards(card_1, card_2):
    """
    Returns the sum of random first two random card drawn
    from player one according to the blackjack game.
    """
    return card_1 + card_2

def busted(usercard_sum, compcard_sum):
    """
    Blackjack rule check to see if player one or computer's
    sum of all cards drawn had gone beyond 21, if correct
    returns "busted" for either player one or computer.
    """
    if usercard_sum > 21:
        return "user busted"
    elif compcard_sum > 21:
        return "comp busted"

def check_if_draws(sum_of_usercard, sum_of_compcard):
    """
    Blackjack rule check to see if sum of player one cars
    is equal to sum of computer's card if correct
    returns "Ties".
    """
    if sum_of_compcard == sum_of_usercard:
        return "Ties"

def winner(sum_of_usercard, sum_of_compcard):
    """
    Blackjack rule check for whose card is more closer to
    21 and returns "Winner" or "Loser".
    """
    if sum_of_compcard > sum_of_usercard:
        return "You Lose :("
    else:
        return "You Win :)"

def score_check(usercard_sum, compcard_sum):
    """
    Black jack over all rules checks.
    """
    if busted(usercard_sum, compcard_sum) == "user busted":
        return "You Lose :("
    elif busted(usercard_sum, compcard_sum) == "comp busted":
        return "Opponent went over. You Win :)"
    if check_if_draws(usercard_sum, compcard_sum) == "Ties":
        return "Its a Tie!!"
    return winner(usercard_sum, compcard_sum)
    
def sum_cardlist(allcard_lists):
    """
    Returns the sum of all cards drawn by any user.
    """
    xum = 0
    for each_item in allcard_lists:
        xum += each_item
    return xum

def comps_turn_blackjack_rule(comp_card_lists):
    """
    Draws another card for computer if sum of first card
    and previous card drawn isn't more than 17 until sum of 
    all card drawn is more than 17, then it stops and returns
    the sum of all computer's card drawn.
    """
    if sum_cardlist(comp_card_lists) < 17:
        comp_card_lists.append(d)
        comps_turn_blackjack_rule(comp_card_lists)
    return comp_card_lists

def user_draws_another_card(list_of_users_drawn_cards):
    next_card = e
    list_of_users_drawn_cards.append(next_card)
    return list_of_users_drawn_cards
    
def ask_user_for_another_card(card):
    if card == 'y':
        another_user_card = user_draws_another_card(user_fst_cardlist)

        print(f"Your cards: {another_user_card}, current score: {sum_cardlist(another_user_card)}")
        print(f"Computer's first card: {comp_fstcrd_first}")
        print("\n")
        # user_card_score = sum_cardlist(another_user_card)
    else:
        another_user_card = another_user_card
        print(another_user_card)
    return another_user_card

def usercard_bust_check(user_cards_list):
    if sum_cardlist(user_cards_list) < 21:
        # print(f"bustcheck: {user_cards_list}")
        return user_cards_list
    else:
        return user_cards_list

user_fst_cardlist = [a, b]

user_fst_cardsums = add_cards(user_fst_cardlist[0], user_fst_cardlist[1])

print(f"    Your cards: {user_fst_cardlist}, current score: {user_fst_cardsums}")
print(f"    Computer's first card: {c}")

comp_fstcrd = [c]
comp_fstcrd_first = [c]
all_comps_card = comps_turn_blackjack_rule(comp_fstcrd)
finalScore_for_all_comps_card = sum_cardlist(all_comps_card)

# print(f"{all_comps_card} = {sum_cardlist(all_comps_card)}")

if_another_card = True

while if_another_card:
    def user_bustcheck():
        print(user_fst_cardlist)
        print("\n")
        another_card = input("Type 'y' to get another card, type 'n' to pass: ")
        another_users_card2 = ask_user_for_another_card(another_card)
        if another_users_card2 == False:
            return False
        
        result = usercard_bust_check(another_users_card2)
        quit_prompt = sum_cardlist(result)
        if quit_prompt > 21:
            global if_another_card
            if_another_card = False
            return result

    another_users_card2 = user_bustcheck()
    if another_users_card2 == False:
        if_another_card = False

user_card2_sum = sum_cardlist(another_users_card2)

check = score_check(user_card2_sum, finalScore_for_all_comps_card)

print(f"    Your final hand: {another_users_card2}, final score: {user_card2_sum}")
print(f"    Computer's final hand: {all_comps_card}, final score: {finalScore_for_all_comps_card} ")
print(check)



    # if another_card == 'n':
    # print(f"    Your final hand: {another_user_card}, final score: {user_card_score}")
    # print(f"    Computer's final hand: {all_comps_card}, final score: {finalScore_for_all_comps_card} ")
    # check = score_check(user_card_score, finalScore_for_all_comps_card)
    # print(check)
