#Objective:
# You will build a tip calculator. 
# The inputs to the program are the total bill cost, 
# Percentage tip, 
# and number of people who will split the bill
# The output would be an even split of the cost and calculated tip amongst each of the members

print("Welcome to the top calculator")
subtotal_bill = float(input("What was the total bill? $"))
tip_percent = int(input("What percentage tip would you like to give? 10, 12, or 15%? "))
num_persons = int(input("How many people to split the bill? "))

indiv_bill = round(subtotal_bill*(1 + tip_percent/100)/num_persons, 2)

print(f"Each person should pay: ${indiv_bill}")
