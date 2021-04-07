#Rock Paper Scissors Game
# 0 = Rock, 1 = Paper, 2 = Scissors

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

print("Welcome to the rock-paper-scissors game. Please select a number choice: \n 0 = Rock\n 1 = Paper\n 2 = Scissors")
player_choice = input("What do you choose? ")
player_choice = int(player_choice)
