MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 150,
    "coffee": 100,
    "Money": 0
}

ended = False
#deficient = False
#TODO 1: prompt user asking what would you like?
while not ended:
    deficient = False
    selection = input("What would you like? (espresso/latte/cappuccino):")
    # TODO 2: Check if resources are sufficient - after asking what the user wants. If resources are suffiient, ask the user for coins 
    if selection in list(MENU.keys()): #if they are asking for a drink
        print(f"Btdubs, a {selection} costs {MENU[selection]['cost']}")
        required_resources = MENU[selection]['ingredients']
        cost = MENU[selection]['cost']
        for ingredient in required_resources:
            if resources[ingredient] < required_resources[ingredient]:
                print(f"Sorry, there is not enough {ingredient}")
                deficient = True
                break
                #ended = True
        if not deficient: 
            print("Please insert coins.")
            quarters = int(input("How many quarters?: "))
            dimes = int(input("How many dimes?: "))
            nickels = int(input("How many nickels?: "))
            pennies = int(input("How many pennies?: "))
            total_amount = quarters * 0.25 + dimes*0.10 + nickels * 0.05 + pennies * 0.01
            print(f"Total amount entered is: ${total_amount}")
            # TODO 5: Check if sufficient coins - calculate monetary value of coins inserted, check if enough. if not, print sorry message with refund
            # TODO 6: if enough money, return drink, deplete resources, add money to resources 
            if total_amount >= MENU[selection]['cost']:
                change = total_amount - MENU[selection]['cost']
                if change > 0: 
                    print(f"Here's your change ${change}")
                for key in required_resources:
                    resources[key] -= required_resources[key]
                resources['Money'] += MENU[selection]['cost']
                #TODO 7: once resources have been deducted, send user their drink and wish them well to enjoy. Then start program again for next customer with present resources 
                print(f"Here's your {selection}, Enjoy!")
            else:
                print("Sorry that is not enough money. Money refunded!")
# TODO 3: when user types report - print the current state of resources
    elif selection == 'report':
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${resources['Money']}")
    #TODO 4: when user types off - stop the program - end immediately 
    elif selection == 'off':
        ended = True
    else: 
        print("Invalid selection. Please restart.")