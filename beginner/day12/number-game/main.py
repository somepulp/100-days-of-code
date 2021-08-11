
from art import logo 
import random
EASY_LEVEL_GUESS = 10
HARD_LEVEL_GUESS = 5

def guess_checker_minus(guess, answer, count):
     if guess != answer:
          if guess > answer:
               print("Too high")
          else:
               print("Too low")
          return count - 1 
     else:
          print(f"You got it! The answer was {answer}")

def computer_whisperer():
     print(logo)
     print("Welcome to Computer Whisperer\u2122\nI am the computer, you are my muse...well only if you can read my mind ;)\nI'm thinking of a number between 1 and 100, can you guess what it is?\nDifficulty levels: 1. Easy, or 2. Hard.\n")
     
     computer_number = random.randint(1,100)
     user_input  = input("Type 1 or 2 to select your difficulty level: ")
     guess_count = EASY_LEVEL_GUESS if user_input == '1' else HARD_LEVEL_GUESS
     print(f"for testing purposes, the number is {computer_number}")
     
     while guess_count > 0:
          print(f"You have {guess_count} guesses remaining")
          user_guess = input("Guess a number: ")
          while not user_guess.isnumeric():
               user_guess = input("Invalid input! Please guess a number: ")
          user_guess = int(user_guess)
          
          guess_count = guess_checker_minus(user_guess, computer_number, guess_count)
          if user_guess == computer_number:
               guess_count = -1
          if guess_count == 0:
               print("You have run out of guesses, you lose")
          

     play_again = input("Do you want to play again? Type 'yes' or 'no': ")
     if play_again == 'yes':
          computer_whisperer()

computer_whisperer()