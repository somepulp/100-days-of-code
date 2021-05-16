#TODO 1: import art, create welcome message
from art import logo 
import random
print(logo)
print("Welcome to Computer Whisperer\u2122\nI am the computer, you are my muse...well only if you can read my mind\nI'm thinking of a number between 1 and 100, can you guess what it is?\nLevels: 1. Easy, or 2. Hard.\n")

#TODO 2: select a number between 1 and 100 for the computer
computer_number = random.randint(1,100)
#TODO 3: create variable for guesses, based on whether the user selects easy or hard. easy = 10 guesses, hard = 5
guess_dict = {
     'easy': 10,
     'hard': 5
}
user_input  = input("Type 1 or 2 to select your difficulty level: ")
diff = 'easy' if user_input == '1' else 'hard'
user_guesses = guess_dict[diff]
#TODO 4: if user guesses wrong, decrement guess variable by 1 -- need while loop
