# Paint Area Calculator
# 1 can of paint covers 5 square meters. Given a random height and width of a wall,
# calculate how many cans of paint you need to buy

# import packages
import math

# function definition
def paint_calc(height, width, cover):
     paint_needed = math.ceil(height * width / cover)
     message = print(f"You'll need {paint_needed} cans of paint.")
     return(message)



#Write your code above this line 👆
# Define a function called paint_calc() so that the code below works.   

# 🚨 Don't change the code below 👇
test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)
