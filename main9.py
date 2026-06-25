import os
from art import logo

# Custom clear function for VS Code terminal
def clear():
    # 'cls' is for Windows, 'clear' is for Mac and Linux
    os.system('cls' if os.name == 'nt' else 'clear')

bids = {}
bidding_finished = False

def find_highest_bidder(bid_record):
    highest_bid = 0
    winner = ""
    for bidder in bid_record:
        bid_amount = bid_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}.")

# Application Start
print(logo)
print("Welcome to the secret auction program.")

while not bidding_finished:
    name = input("What is your name?: ")
    price = int(input("What's your bid?: $"))
    bids[name] = price
    
    should_continue = input("Are there any other bidders? Type 'yes' or 'no'.\n").lower()
    clear()
    
    if should_continue == "no":
        bidding_finished = True
        find_highest_bidder(bids)