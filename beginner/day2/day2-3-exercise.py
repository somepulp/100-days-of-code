# Create a program that tells you how many days, weeks, months and years a user has left if they live 
# until 90 years old

#input - current age
# output - message with the time left in this format: "You have x days, y weeks and z months left"


print("This program will tell you how much time you have left until you are 90 years old")
age = input("What is your current age? ")

#365 days in a year, 52 weeks in a year and 12 months in a year

years_left = 90 - int(age)
weeks_left = years_left*52
months_left = years_left*12
days_left = years_left*365

print(f"You have {years_left} years left, or {months_left} months, or {weeks_left} weeks or {days_left} days until you are 90 years old")