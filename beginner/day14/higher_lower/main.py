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
    elif user_input == "B":
        correct = person_B_dict["follower_count"] > person_A_dict["follower_count"]
    else:
        correct = False
    return(correct)

def higher_lower():
    #TODO 1: print ascii art for higher lower
    print(logo)
    #TODO 2: get random item from game_data - person_A - create random selector function
    
    competitors = random_selections(lst = data, n = 2)
    person_A = competitors[0]
    person_B = competitors[1]
    correct_count = 0 
    game_continue = True

    #TODO 3: extract name, description, country from random item
    while game_continue:
        
        print(f'Compare A: {person_A["name"]}, a {person_A["description"]}, from {person_A["country"]}.')
        
        print(vs)
        #TODO 4: get another random item from game_data that is not same as previous item - person_B
        # 
        print(f'Against B: {person_B["name"]}, a {person_B["description"]}, from {person_B["country"]}.')
        #TODO 5: ask user who has more followers 'A' or 'B'

        user_input = input("Who has more followers? Type 'A' or 'B': ").capitalize()
        
        #TODO 6: check if user is right: if user_input = 'A', does person_A.followers > person_B.followers?
        #if user_input = "B" does person_B.followers > person_A.followers? 
        #TODO 6.5: create function that outputs true if user is right, false if user is wrong or they did not type A or B


        #TODO 7: if user is right, person A becomes the first person in competitor list. person b is another random person
        if user_correct(user_input = user_input, person_A_dict = person_A, person_B_dict = person_B):
            correct_count += 1
            competitors[0] = competitors[1]
            competitors[1] = random_selections(lst = data, n=1)
        else:
            game_continue = False

#TODO 8: loop through - if user is right 