# Prime Number checker

# According to wikipedia:
#The simplest primality test is trial division: 
# given an input number, n, check whether it is evenly divisible by any prime number between 2 and √n 
# (i.e. that the division leaves no remainder). If so, then n is composite. Otherwise, it is prime.[1]

import math

def prime_checker(number):
     is_prime = True
     # check if it divisible by any number between 2 and its square root
     sqroot = math.sqrt(number)
     for num in range(2, int(sqroot)+1):
          if number % num == 0:
                is_prime = False
     if not is_prime:
          print("It's not a prime number")
     else:
          print("It's a prime number")

n = int(input("Check this number: "))
prime_checker(number=n)

## Tests: prime numbers from 1 to 100:
prime_list = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
for num in prime_list:
     prime_checker(num)