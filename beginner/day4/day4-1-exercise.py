# Virtual Coin Toss Program
# This will randomly tell the user whether to select "Heads" or "Tails"
# Generate a random number, either 0 or 1, then use that number to print out heads or tails

# Can use the round function with a random float number between 0 and 1:
import random
print("Welcome to the Virtual Toin Coss program. The side we ended up on is:")

rand_float = random.random()
digit = round(rand_float)

if digit < 1:
    print("Tails")
else:
    print("Heads")