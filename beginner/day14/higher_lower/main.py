from random import choice, sample
from art import logo, vs
from game_data import data

# Functions:
def random_selections(lst, n):
    if n == 1:
        return(choice(lst))
    if n == 2:
        return(sample(lst, k=n))

def user_correct(user_input, person_A_dict, person_B_dict):
    if user_input == "A":
        correct = person_A_dict["follower_count"] > person_B_dict["follower_count"]
        dict = person_A_dict
    elif user_input == "B":
        correct = person_B_dict["follower_count"] > person_A_dict["follower_count"]
        dict = person_B_dict
    else:
        correct = False
    return( {
        "correct": correct,
        "selected": dict
        })

def higher_lower():
    print(logo)

    competitors = random_selections(lst = data, n = 2)
    person_A = competitors[0]
    person_B = competitors[1]
    correct_count = 0 
    game_continue = True

    while game_continue:

        print(f'Compare A: {person_A["name"]}, a {person_A["description"]}, from {person_A["country"]}.')
        print(vs)
        print(f'Against B: {person_B["name"]}, a {person_B["description"]}, from {person_B["country"]}.')

        user_input = input("Who has more followers? Type 'A' or 'B': ").capitalize()

        #TODO 7: if user is right, person A becomes the first person in competitor list. person b is another random person
        user_result = user_correct(user_input = user_input, person_A_dict = person_A, person_B_dict = person_B)
        if user_result["correct"]:
            correct_count += 1
            person_A = user_result["selected"]
            person_B = random_selections(lst=data, n=1)
            print(f"You're right! Current score: {correct_count}")
        else:
            game_continue = False
            print(f"Wrong! Game over. Your final score was {correct_count}")


higher_lower()