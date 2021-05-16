
from art import logo 
import random

def computer_whisperer():
     print(logo)
     print("Welcome to Computer Whisperer\u2122\nI am the computer, you are my muse...well only if you can read my mind\nI'm thinking of a number between 1 and 100, can you guess what it is?\nLevels: 1. Easy, or 2. Hard.\n")
     
     guess_dict = {
          'easy': 10,
          'hard': 5
     }
     
     computer_number = random.randint(1,100)
     user_input  = input("Type 1 or 2 to select your difficulty level: ")
     diff = 'easy' if user_input == '1' else 'hard'
     guess_count = guess_dict[diff]
     print(f"for testing purposes, the number is {computer_number}")
     
     while guess_count > 0:
          #TODO 5: print the number of guesses the user has remaining
          print(f"You have {guess_count} guesses remaining")
          #TODO 6: ask them to guess
          user_guess = int(input("Guess a number: "))
          #TODO 7: check whether they are right or not. If they are wrong, tell them if their guess is too high or too low
          if user_guess != computer_number:
               #TODO 8: ask them to guess again, and decrement their remaining guesses by 1
               if user_guess > computer_number:
                    print("Too high")
               else:
                    print("Too low")
               guess_count -= 1
               if guess_count == 0:
                    print("You have run out of guesses, you lose")
          else:
               print(f"You got it! The answer was {computer_number}")
               guess_count = -1

     play_again = input("Do you want to play again, type 'yes' or 'no': ")
     if play_again == 'yes':
          computer_whisperer()

computer_whisperer()