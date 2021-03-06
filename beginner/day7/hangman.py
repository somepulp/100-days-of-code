# Importing modules: 
import random
#import ascii art 
from hangman_art import stages, logo
#import words list 
from hangman_words import word_list

# initializing variables 
chosen_word = random.choice(word_list) 
word_length = len(chosen_word)
end_of_game = False
lives = len(stages) - 1

# Printing logo at the start of the game
print(logo)

# Create blanks
display = []
for c in range(word_length): 
    display += "_"

while not end_of_game:
    # user guess, converted to lower case
    guess = input("Guess a letter: ").lower()
    # if they have already guessed the letter, tell them to try again. if not, perform checks
    if guess in display:
        print(f"Guess another letter, you already found {guess}! ")
    # if the letter is not in the chosen word, lives reduce by 1, and we print a notification 
    elif guess not in chosen_word: 
        print(f"{guess} is not in the chosen word!")
        lives -=1 
        # if lives goes down to 0, the game is over
        if lives == 0:
            end_of_game = True
            print(f"You have no more lives. You lose.\nThe word was {chosen_word}")
    # if they find a letter in the chosen_word
    else:
        # Replace blanks with letter if guess is found 
        for i in range(word_length):
            if guess == chosen_word[i]:
                display[i] = guess

    
    #Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")
    
    #print(display)

    if "_" not in display:
        end_of_game = True
        print("You won!")
    
    #print the ASCII art from 'stages' that corresponds to the current number of 'lives' the user has remaining.
    print(stages[lives])