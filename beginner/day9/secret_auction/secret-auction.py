# Importing Packages
import os
from art import logo

# clear function
clear = lambda: os.system('clear')

#initializing variables
print(logo)
print("Welcome to the secret auction program")
more_bids = True
customer_list = []

while more_bids == True:
     name = input("What is your name?: ")
     bid = input("What is your bid?: $")
     more_bidders = input("Are there any other bidders? Type 'yes' or 'no'.\n")

     new_bid = {}
     new_bid['customer_name'] = name
     new_bid['bid_amount'] = bid

     customer_list.append(new_bid)

     if more_bidders == 'no':
          more_bids = False
     else:
          clear()

max_bid = customer_list[0]['bid_amount']
bid_winner = customer_list[0]['customer_name']
for item in customer_list:
     if item['bid_amount'] > max_bid:
          max_bid = item['bid_amount']
          bid_winner = item['customer_name']
clear()

print(f"The winner is {bid_winner} with a bid of ${max_bid}")
