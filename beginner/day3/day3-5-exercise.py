## This program tests the compatibility of two people using a method recommended by BuzzFeed
#take both people's names and check for the number of times the letters in the word TRUE occurs.
# then check for the number of times the letters in the word LOVE occurs
# combine these numbers to make a two digit number

# Welcome message
print("Welcome to the 'Love Calculator'!")
# first name
name1 = input("What is the first name? \n")
name2 = input("What is the second name? \n")


#check for number of times the letters in the word TRUE occurs 
sname1 = name1.lower()
sname2 = name2.lower()
combined_name = sname1+sname2
first_digit = combined_name.count("t") + combined_name.count("r") + combined_name.count("u") + combined_name.count("e")
second_digit = combined_name.count("l") + combined_name.count("o") + combined_name.count("v") + combined_name.count("e")

#combine both digits to get love score
love_score = int(str(first_digit)+str(second_digit))

# score thresholds:
# if score is less than 10 or greater than 90, message: 'Your score is x, you go together like coke and mentos'
# if score is between 40 and 50, message: "Your score is y, you are alright together"
# otherwise, message: "Your score is z."

if love_score < 10 or love_score > 90:
    print(f"Your score is {love_score}, you go together like coke and mentos")
elif love_score >= 40 and love_score <= 50:
    print(f"Your score is {love_score}, you are alright together")
else:
    print(f"Your score is {love_score}.")