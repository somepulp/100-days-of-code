#Today we learn about: 
# - conditional statements
# - logical operators
# - code blocks
# - scope, global and local name spacing 
# at the end of the day we will build a simple choose your own adventure game 

## Conditional Statements - ifelse
# if condition:
#     do this
# else:
#     do this

# Rollercoaster ifelse
print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

# if height < 120:
#     print("You cannot ride the rollercoaster! You are too short, scram!")
# else:
#     print("Come on board you giant!")

## Comparison operators: <, <=, >, >=, ==, != 

## More complex ways of using if and else statements: Nested ifelse statements

# if condition:
#     if another condition:
#         do this
#     else: 
#         do this
# else:
#     do this

# also we can use *elif* to further complicate our if statements 
# if condition:
#     if another condition:
#         do this
#     elif: 
#         do this
#     else: 
#         do this
# else:
#     do this
# we want to nest a condition depending on the age of the rider
age = int(input("What is your age? "))

# if height < 120:
#     print("You cannot ride the rollercoaster! You are too short, scram!")
# else:
#     if age > 18:
#         ticket = 12
#     elif age < 12:
#         ticket = 5
#     else:
#         ticket = 7
#     print(f"Come on board you giant! You need to pay ${ticket}")


## With if statements, you generally check and end at one condition, if you want to have multiple conditions checked,
## use multiple if statements, rather than multiple elif statements. That way each condition you need to be checked will be checked.
## i.e. use the following structure:
# if condition1: 
#     do A
# if condition2:
#     do B
# if condition3:
#     do C

##Let's say we want to provide them with the option to buy a photo, which will cost $3

# if height < 120:
#     print("You cannot ride the rollercoaster! You are too short, scram!")
# else:
#     if age > 18:
#         bill = 12
#         print("Adult tickets are $12")
#     elif age < 12:
#         bill = 5
#         print("Child tickets are $5")
#     else:
#         bill = 7
#         print("Youth tickets are $7")
#     want_photo = input("Do you want a photo taken? Y or N: ")
#     if want_photo == "Y":
#         bill+=3
#     print(f"Come on board you giant! You need to pay ${bill}")


################ 
#Logical Operators: and, or, not
a = 12
not a > 15

#add condition to code to give people aged between 45-55 a free ride

if height < 120:
    print("You cannot ride the rollercoaster! You are too short, scram!")
else:
    if age >= 45 and age <= 55:
        bill = 0
        print("You get a ride for free, mid-life crisis-san")
    elif age > 18:
        bill = 12
        print("Adult tickets are $12")
    elif age < 12:
        bill = 5
        print("Child tickets are $5")
    else:
        bill = 7
        print("Youth tickets are $7")
    want_photo = input("Do you want a photo taken? Y or N: ")
    if want_photo == "Y":
        bill+=3
    print(f"Come on board you giant! You need to pay ${bill}")