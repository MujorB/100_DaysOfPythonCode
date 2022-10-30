#! /usr/bin/python3

"""
Black Jack Game, Day 11 of 100daysOfCode Capstone Project.
"""
import art
import random

print(art.logo)
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def draw():
    """
    Draw and returns a random card from the card list without
    removing the card drawn from the list.
    """
    return random.choice(cards)


def is_blackjack(comp_totalcardlist, user_totalcardlist):
    """
    Check if the sum of computers card or user's card
    is exactly equal 21, returns "Blackjack You Lose :("
    if computers score is 21 else returns "Blackjack You
    Win :)" if users score is equal 21.
    """
    if comp_totalcardlist == 21:
        return "Blackjack You Lose :("
    elif user_totalcardlist == 21:
        return "Blackjack You Win :)"
    elif user_totalcardlist > 21:
        return "You went Overboard, You Lose :("
    elif comp_totalcardlist == user_totalcardlist:
        return "Its a Tie!!"
    else:
        if user_totalcardlist < 21 and user_totalcardlist > comp_totalcardlist:
            return "You Win :)"
        elif comp_totalcardlist > 21:
            return "Opponent Went Overboard, You Win :)"
        else:
            return "You Lose"


def sum_cardlist(allcard_lists):
    """
    Returns the sum of all cards drawn by any user.
    """
    xum = 0
    for each_item in allcard_lists:
        xum += each_item
    return xum


def comps_play_turn(comp_card_lists):
    """
    Draws another card for computer if sum of first card
    and previous card drawn isn't more than 17 until sum of
    all card drawn is more than 17, then it stops and returns
    the sum of all computer's card drawn.
    """
    if sum_cardlist(comp_card_lists) < 17:
        comp_card_lists.append(draw())
        comps_play_turn(comp_card_lists)
    return comp_card_lists


def user_wants_another_card(list_of_users_drawn_cards):
    list_of_users_drawn_cards.append(draw())
    return list_of_users_drawn_cards


def wantMoreCards():
    anotherCard = True
    user_fst_cardlist_1 = user_fst_cardlist
    while anotherCard:
        want_moreCards = input("Type 'y' to get another card, \
type 'n' to pass: ")
        if want_moreCards == 'y':
            user_fst_cardlist_1 = user_wants_another_card(user_fst_cardlist)
            print(f"    Your cards: {user_fst_cardlist_1}, current score: \
{sum_cardlist(user_fst_cardlist_1)}")
            print(f"    Computer's first card: {comps_firstcard}\n")
        else:
            anotherCard = False
    return user_fst_cardlist_1


a = draw()
play_blackjack_again = True

while play_blackjack_again:
    user_fst_cardlist = [draw(), draw()]
    user_cardlist_sums = sum_cardlist(user_fst_cardlist)

    comps_firstcard = a

    print(f"    Your cards: {user_fst_cardlist}, current score: \
{user_cardlist_sums}")
    print(f"    Computer's first card: {comps_firstcard}\n")

    comp_fst_cardlist = [comps_firstcard]
    comp_cardlist_sums = sum_cardlist(comp_fst_cardlist)

    more_usercards = wantMoreCards()
    user_cardlist_sums_2 = sum_cardlist(more_usercards)

    comp_fst_cardlist_2 = comps_play_turn(comp_fst_cardlist)
    comp_cardlist_sums_2 = sum_cardlist(comp_fst_cardlist_2)

    scores_check = is_blackjack(comp_cardlist_sums_2, user_cardlist_sums_2)

    print(f"    Your final hand: {more_usercards}, final score: \
{user_cardlist_sums_2}")
    print(f"    Computer's final hand: {comp_fst_cardlist_2}, final score: \
{comp_cardlist_sums_2} ")
    print(scores_check)
    print("\n")

    wanna_play_again = input("Do you want to play a game of Blackjack? \
Type 'y' or 'n': ")
    print(f"\n" * 30, f"{art.logo}\n\n")
    a = draw()
    if wanna_play_again == "n":
        play_blackjack_again = False
    else:
        continue

# Phewwwww! at last :) .....
