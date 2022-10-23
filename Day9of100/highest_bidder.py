#! /usr/bin/python3
import auction_art

# from replit import clear
# HINT: You can call clear() to clear the output in the console.

message = "Welcome to the secret auction program."
question = True
print(auction_art.logo + "\n" + message)

bidders_logs = {}

def enter_bidders_log():
    name = input("What is your name?: ")
    bid = int(input("What's your bid?: $"))
    bidders_logs[name] = bid

while(question):
    enter_bidders_log()
    reply = input("Are there any bidders? Type 'yes' or 'no'\n")

    if reply == "no":
        question = False
    elif reply != "yes":
        print("please enter 'yes' or 'no'")
        continue

first_bid = 0

for highest_bidder in bidders_logs:
    if bidders_logs[highest_bidder] > first_bid:
        first_bid = bidders_logs[highest_bidder]
        bidder_name = str(highest_bidder)
print(f"The winner is {bidder_name} with a bid of ${first_bid}.")
