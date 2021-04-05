#Write a program that will select a random name from a list of names. 
# The person selected will have to pay for everybody's food bill
import random
# Split string method
print("Welcome to Banker's Roulette, where we force one person to pay for the bill :)")
names_string = input("Give me everybody's names, separated by a comma: ")
names = names_string.split(", ")
#the split method allows you to split a string into a list using a divider

#given a list of names, we need to just select a random person - random index - random number
num_people = len(names)
random_index = random.randint(0,num_people-1)
selected_culprit = names[random_index]

print(f"{selected_culprit} is responsible for the bill today!")
