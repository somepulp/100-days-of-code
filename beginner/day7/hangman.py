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

# user guess, converted to lower case
guess = input("Guess a letter: ").lower()

# Replace blanks with letter if guess is found 
for i in range(word_length):
    if guess == chosen_word[i]:
        display[i] = guess

print(display)