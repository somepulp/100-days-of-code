# Importing packages: 
import random

word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list) 
word_length = len(chosen_word)

#Testing code
print(f'Pssst, the solution is {chosen_word}.')

# Create blanks
display = []
for c in range(word_length): 
    display += "_"

#TODO-1: - Use a while loop to let the user guess again. The loop should only stop once the user has
#          guessed all the letters in the chosen_word and 'display' has no more blanks ("_"). 
#          Then you can tell the user they've won.

end_of_game = False
while not end_of_game:
    # user guess, converted to lower case
    guess = input("Guess a letter: ").lower()
    # if they have already guessed the letter, tell them to try again. if not, perform checks
    if guess in display:
        print(f"Guess another letter, you already tried {guess}! ")
    else:
        # Replace blanks with letter if guess is found 
        for i in range(word_length):
            if guess == chosen_word[i]:
                display[i] = guess
    
    print(display)
    
    if "_" not in display:
        end_of_game = True
        print("You won!")
