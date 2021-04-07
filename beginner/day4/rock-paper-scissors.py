#Rock Paper Scissors Game
# 0 = Rock, 1 = Paper, 2 = Scissors
# importing required modules
import random
#Ascii art 😝 
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
choice_list = [["rock", "paper", "scissors"],[rock, paper, scissors]]

print("Welcome to the rock-paper-scissors game. Please select a number choice: \n 0 = Rock\n 1 = Paper\n 2 = Scissors")
player_num = int(input("What do you choose? "))
player_choice = choice_list[0][player_num]
player_ascii = choice_list[1][player_num]

#Error checking
if(player_choice > 2):
    print("You have selected an invalid number. Please select 0 for Rock, 1 for Paper, or 2 for Scissors")
else:
    computer_num = random.randint(0,2)
    computer_choice = choice_list[0][computer_num]
    computer_ascii = choice_list[1][computer_num]
    # paper beats rock (1 beats 0 - 1>0)
    # scissors beats paper (2 beats 1 - 2>1)
    # rock beats scissors (0 beats 2 - 0 < 2 )
    if computer_num == player_num:
        print(player_ascii)
        print(f"The computer chose:\n{computer_ascii}")
        print("Issa tieeee!")