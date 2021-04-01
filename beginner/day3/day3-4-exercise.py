#We will be building a pizza order program. 
#User input: 
# - size of pizza: S, M, or L. cost: S: 15, M: 20, L: 25
# - want pepperoni? Y or N. costs: S: 2, M/L:3
# - want extra cheese? Y or N cost: S/M/L: 1

print("Welcome to Ma Pizza Place!")
pizza_size = input("What size of pizza would you like? S, M or L? \n")
want_pepperoni = input("Would you like pepperoni on your pizza? Y or N? \n")
want_more_cheese = input("Would you like extra cheese on your pizza? Y or N? \n")


if pizza_size == "S":
    bill = 15
    if want_pepperoni == "Y":
        bill +=2
elif pizza_size == "M":
    bill = 20
    if want_pepperoni == "Y":
        bill += 3
else:
    bill = 25
    if want_pepperoni == "Y":
        bill += 3

if want_more_cheese == "Y":
    bill += 1

print(f"Your final bill is ${bill}")


############################
# Teacher solution:

tbill = 0

if pizza_size == "S":
    tbill += 15
elif pizza_size == "M":
    tbill += 20
else: 
    tbill += 25

if want_pepperoni == "Y":
    if pizza_size == "S":
        tbill +=2
    else:
        tbill +=3

if want_more_cheese == "Y":
    tbill += 1

print(f"Your final bill is: ${tbill}")