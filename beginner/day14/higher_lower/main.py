from random import choice, random, sample
from art import logo, vs
from game_data import data
import os 

clear = lambda: os.system('clear')

# Functions:
def random_selection():
       return(choice(data))


def user_correct(user_input, person_A_dict, person_B_dict):
    if person_A_dict["follower_count"] > person_B_dict["follower_count"]:
        correct = user_input == "A"
    else:
        correct = user_input == "B"
    return correct

def higher_lower():
    print(logo)

    # person_A = random_selection()
    person_B = random_selection()
    correct_count = 0 
    game_continue = True

    while game_continue:
        person_A = person_B
        person_B = random_selection()

        print(f'Compare A: {person_A["name"]}, a {person_A["description"]}, from {person_A["country"]}.')
        print(vs)
        print(f'Against B: {person_B["name"]}, a {person_B["description"]}, from {person_B["country"]}.')

        user_input = input("Who has more followers? Type 'A' or 'B': ").capitalize()
        clear()
        print(logo)
        #TODO 7: if user is right, person A becomes the first person in competitor list. person b is another random person
        correct = user_correct(user_input = user_input, person_A_dict = person_A, person_B_dict = person_B)
        if correct:
            correct_count += 1
            print(f"You're right! Current score: {correct_count}")
        else:
            game_continue = False
            print(f"Wrong! Game over. Your final score was {correct_count}")


higher_lower()