############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1. (it counts as 1 if the sum with 11 goes over 21)
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.
import os
import random
from art import logo
# clear function
clear = lambda: os.system('clear')

messages = {
    'computer_blackjack': "You lose, the computer has a BlackJack!",
    'user_blackjack': "BlackJack! You won!",
    'user_over_21': "You went over. You lose!",
    'computer_over_21': "You won, because the computer went over 21!",
    'draw': "It's a draw ;)",
    'user_win': "You won!",
    'computer_win': "You lost, the computer won this round"
}

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

#define functions for operations - make these functions independent of user/computer list... 
# i.e take any list and perform operations - extention - maybe create a dictionary of card operations and call?

def deal_card(player_list, num_card = 1):
    for num in range(num_card):
        player_list.append(random.choice(cards))

def replace_ace(player_list):
        player_total = sum(player_list)
        if 11 in player_list and player_total > 21:
                player_list[player_list.index(11)] = 1

def run_blackjack():
    #Start the game off by printing the logo, and initializing the card list, game_continue variable and message dictionary 
    print(logo)
    user_card_list = []
    computer_card_list = []
    game_continue = True
    user_blackjack = False
    computer_blackjack = False
    #blackjack rules 
    def find_winner(user_list, computer_list):
        computer_total = sum(computer_list)
        user_total = sum(user_list)
        if computer_blackjack:
            print(messages['computer_blackjack'])
        elif user_blackjack:
            print(messages['user_blackjack'])
        elif user_total > 21:
            print(messages['user_over_21'])
        elif computer_total > 21:
            print(messages['computer_over_21'])
        elif user_total == computer_total:
            print(messages['draw'])
        elif user_total > computer_total:
            print(messages['user_win'])
        else:
            print(messages['computer_win'])

    # deal both the user and computer a starting hand of 2 random card values
    deal_card(player_list = user_card_list, num_card = 2)
    deal_card(player_list = computer_card_list, num_card = 2)

    while game_continue:
        print(f"Your cards: {user_card_list}, current score: {sum(user_card_list)}")
        print(f"Computer's first card: {computer_card_list[0]}")

        if (len(user_card_list) == 2 and sum(user_card_list) == 21):
            game_continue = False
            user_blackjack = True
        elif sum(user_card_list) > 21:
            game_continue = False
        else:
            draw_again = input("Type 'y' to get another card, type 'n' to pass: ")
            if draw_again == 'y':
                deal_card(player_list = user_card_list)
                replace_ace(player_list= user_card_list)
            else:
                game_continue = False
    
    user_total = sum(user_card_list)
    #play computer once user selection stops
    computer_total = sum(computer_card_list)
    if (len(computer_card_list) == 2 and computer_total == 21):
        computer_blackjack = True
    else:
        while computer_total <= 16:
            deal_card(player_list = computer_card_list)
            replace_ace(player_list = computer_card_list)
            computer_total = sum(computer_card_list)
        
    print(f"Your final hand: {user_card_list}, final score: {user_total}")
    print(f"Computer's final hand: {computer_card_list}. final score: {computer_total}")

    find_winner(user_list = user_card_list, computer_list = computer_card_list)

while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
    clear()
    run_blackjack()

