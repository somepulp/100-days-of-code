# Importing Packages
import os
from art import logo

# clear function
clear = lambda: os.system('clear')

#initializing variables
print(logo)
print("Welcome to the secret auction program")
more_bids = True
customer_bids = {}

def highest_bidder(bidder_dict):
     max_bid = 0
     bid_winner = ""
     for key in bidder_dict:
          bid_amount = bidder_dict[key]
          if bid_amount > max_bid:
               max_bid = bid_amount
               bid_winner = key
     print(f"The winner is {bid_winner} with a bid of ${max_bid}")


while more_bids:
     name = input("What is your name?: ")
     bid = float(input("What is your bid?: $"))
     more_bidders = input("Are there any other bidders? Type 'yes' or 'no'.\n").lower()

     customer_bids[name] = bid

     if more_bidders == 'no':
          clear()
          more_bids = False
          highest_bidder(customer_bids)
     else:
          clear()
