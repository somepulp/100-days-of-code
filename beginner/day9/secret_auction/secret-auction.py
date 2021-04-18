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

while more_bids == True:
     name = input("What is your name?: ")
     bid = float(input("What is your bid?: $"))
     more_bidders = input("Are there any other bidders? Type 'yes' or 'no'.\n").lower()

     #new_bid = {}
     customer_bids[name] = bid
     #new_bid['bid_amount'] = bid

     #customer_list.appendl(new_bid)

     if more_bidders == 'no':
          more_bids = False
     else:
          clear()

#max_bid = customer_bids[0]['bid_amount']
#bid_winner = customer_list[0]['customer_name']
max_bid = 0
bid_winner = ""

for key in customer_bids:
     if customer_bids[key] > max_bid:
          max_bid = customer_bids[key]
          bid_winner = key

max_bid = round(max_bid,2)
clear()

print(f"The winner is {bid_winner} with a bid of ${max_bid}")
