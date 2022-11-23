#! /usr/bin/env python3

"""
Purpose:    Making a coffee machine.
Course:     100 days of python code by Angela Yu <day 15>
Date:        Mon, Nov 14, 2022.
"""

import coffee_machine_art


def coffee_request():
    """Prompts user for the type of coffee needed and returns the coffee type"""

    def report_command(command):
        """Checks for the machine command "report" and returns the status of machine resource"""
        if command == "report":
            print(machines_report())

    coffee_type = input(" What would you like? (espresso/latte/cappuccino): ")
    coffee_list = ["espresso", "latte", "cappuccino", "report", "off"]
    if coffee_type not in coffee_list:
        sorry = f" \tSorry '{coffee_type}' is not available\n"
        message = " please enter: 'espresso', 'latte' or 'cappuccino'\n"
        print(sorry + message)
        coffee_type = coffee_request()
    elif coffee_type == "report":
        report_command(coffee_type)
        coffee_type = coffee_request()
    elif coffee_type == "off":
        global machine_runs
        machine_runs = False
        return "\n Turning off . . .\n\tBYE\n\n"
    return coffee_type


def resource_sufficiency(users_coffee_request):
    """
    Purpose:    Collects user coffee type request and checks against
                available coffee machine resources.
    Returns:    If coffee type resource is not enough or available,
                Its notify the user and returns False else it returns
                True.
    """
    available_water_resource = resources["water"]
    available_coffee_resource = resources["coffee"]
    available_milk_resource = resources["milk"]
    error_message = ""
    users_milk = MENU[users_coffee_request]["ingredients"]["milk"]
    users_water = MENU[users_coffee_request]["ingredients"]["water"]
    users_coffee = MENU[users_coffee_request]["ingredients"]["coffee"]

    for coffee_type in MENU:
        if users_coffee_request == coffee_type:
            if users_water > available_water_resource:
                error_message = "Sorry there is not enough water\n\n"
            elif users_coffee > available_coffee_resource:
                error_message = "Sorry there is not enough coffee\n\n"
            elif users_milk > available_milk_resource:
                error_message = "Sorry there is not enough milk\n\n"
            if "Sorry" in error_message:
                print(error_message)
                return False
            return True


def user_currency():
    """Function that calculates the user's coins and returns it values in dollars"""
    print("Please insert coins")
    quarter_coins = int(input("how many quarters?: "))
    dime_coins = int(input("how many dimes?: "))
    nickel_coins = int(input("how many nickels?: "))
    penny_coins = int(input("how many pennies?: "))
    coins_value = quarter_coins * 0.25 + dime_coins * 0.1 + nickel_coins \
                  * 0.05 + penny_coins * 0.01
    return coins_value


def users_currency_checks(users_coins_value, users_coffee_request):
    """
    Purpose:    Checks user's coins against users against
                coffee type to see if enough or sufficient.
    Return:     If user's currency value is not enough returns
                -1, if the same returns zero and if more returns
                remaining change.
    """
    user_coffee_cost = MENU[users_coffee_request]["cost"]

    if users_coins_value == user_coffee_cost:
        change = 0
    elif users_coins_value > user_coffee_cost:
        change = round(users_coins_value - user_coffee_cost, 2)
    else:
        change = -1
    return change


def compliment(users_coffee_request, users_currency_check, menu):
    """Return a complimentary message on successfully made transaction"""
    message = f"\tHere is your {users_coffee_request} coffee_emoji. Enjoy!"
    if users_currency_check < 0:
        message = "Sorry that's not enough money. Money refunded."
    elif users_currency_check == 0:
        update_machine_resources(users_coffee_request, menu)
    else:
        update_machine_resources(users_coffee_request, menu)
        print(f" Here is ${users_currency_check} in change")
    return message


def update_machine_resources(users_coffee_request, menu):
    """Returns updated coffee machine resources"""
    global profit
    update_water = resources["water"] - menu[users_coffee_request]["ingredients"]["water"]
    update_milk = resources["milk"] - menu[users_coffee_request]["ingredients"]["milk"]
    update_coffee = resources["coffee"] - menu[users_coffee_request]["ingredients"]["coffee"]

    profit += menu[users_coffee_request]["cost"]
    resources["water"] = update_water
    resources["milk"] = update_milk
    resources["coffee"] = update_coffee


def machines_report():
    """Communicates the status of the coffee machine resources"""
    report = f'Water: {resources["water"]}ml\nMilk: {resources["milk"]}ml' \
             f'\nCoffee: {resources["coffee"]}g\nMoney: ${profit}'
    return report


MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
            "milk": 0,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}
profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

# Game main control flow
machine_runs = True
print(coffee_machine_art.logo)
while machine_runs:
    user_coffee_request = coffee_request()
    if "off" in user_coffee_request:
        print(user_coffee_request)
        machine_runs = False
        continue

    resources_checks = resource_sufficiency(user_coffee_request)
    if not resources_checks:
        continue

    user_currency_request = user_currency()
    coins_value_check = users_currency_checks(user_currency_request, user_coffee_request)

    print(compliment(user_coffee_request, coins_value_check, MENU))
    print("\n\n")
