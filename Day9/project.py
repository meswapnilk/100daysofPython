import imp
from art import logo



bidders = {}
new_bidders = "yes"
while(new_bidders == "yes"):
    print("Welcome to blind bidding!")
    print(logo)
    name = input("What is your name?")
    bid = int(input("What's your bid? $"))
    bidders[name] = bid
    new_bidders = input("Are there any other bidders? Type 'yes' or 'no'")

bidder_name = ""
bid = 0
for name in bidders:
    if bid < bidders[name]:
        bid = bidders[name]
        bidder_name = name

print(f"The winner is {bidder_name} with a bid of ${bid}")