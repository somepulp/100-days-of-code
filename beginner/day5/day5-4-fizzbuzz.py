# Fizzbuzz game
# Start off counting to 100 from 1. 
# When you encounter a number fully divisible by 3, change it to "Fizz"
# - if the number is fully divisible by 5, change it to "Buzz"
# - if it is divisible by both, change it to "FizzBuzz"
# Program will print out numbers or characters based on these conditions, from 1 all the way to 100

for number in range(1, 101, 1):
    if number % 15 == 0:
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)