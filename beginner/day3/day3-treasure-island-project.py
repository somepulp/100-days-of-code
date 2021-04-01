
# We will create a treasure island game. 
print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 
left_or_right = input("You have come to a crossroad - choose to go either 'left' or 'right': \n")
isLeft = left_or_right.lower() == "left"
if isLeft == True: 
    swim_or_wait = input("You are now by the water, you can choose to swim across or wait: \n")
    isSwim = swim_or_wait.lower() == "swim"
    if isSwim == False:
        door_choice = input("Nice. A boat came and picked you up. You have been transported to the other side. \nYou now approach a house with three doors\nWhich do you pick, the 'red', 'blue' or the 'yellow' door?:\n")
        if door_choice.lower() == "red" or door_choice.lower() == "blue":
            print("You have been eaten by a hungry lion behind the door you selected. Poor form! ")
        elif door_choice.lower() != "red" and door_choice.lower() != "blue" and door_choice.lower() != "yellow":
            print('You dumb, or you mistyped. Please select an appropriate answer, when you try again. Dumbass.')
        else: 
            print("You won a whopping treasure of shit. Congrats! ")
            print('''
              (   )
            (   ) (
              ) _   )
               ( \_
             _(_\ \)__
            (____\___))  
            ''')
    else:
        print("You have chosen death by water. Try again!")
else: 
    print("You have chosen wrongly. A monster appears and bites your head off. Try again!")