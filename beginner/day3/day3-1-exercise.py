# Odd or Even
# this program works out whether a given number is an odd or even numbers. 
# Hint: even numbers are divisible by 2 with no remainder
# The modulo operator in python is the percentage sign: % 
# it returns the remainder of dividing a nubmer by another

num_input = int(input("Select a number: "))
isEven = num_input%2 == 0

if isEven:
    print(f"{num_input} is an even number")
else:
    print(f"{num_input} is an odd number")