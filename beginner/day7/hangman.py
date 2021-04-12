# Importing packages: 
import random

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

end_of_game = False
word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list) 
word_length = len(chosen_word)

#TODO-1: - Create a variable called 'lives' to keep track of the number of lives left. 
#Set 'lives' to equal 6.
lives = len(stages) - 1

#Testing code
print(f'Pssst, the solution is {chosen_word}.')

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
    elif guess not in chosen_word: 
        lives -=1 
        if lives == 0:
            end_of_game = True
            print("You have no more lives. You lose.")
    else:
        # Replace blanks with letter if guess is found 
        for i in range(word_length):
            if guess == chosen_word[i]:
                display[i] = guess
    
    #TODO-2: - If guess is not a letter in the chosen_word,
    #Then reduce 'lives' by 1. 
    #If lives goes down to 0 then the game should stop and it should print "You lose."
    
    #Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")
    
    #print(display)

    if "_" not in display:
        end_of_game = True
        print("You won!")
    
    #TODO-3: - print the ASCII art from 'stages' that corresponds to the current number of 'lives' the user has remaining.
    print(stages[lives])