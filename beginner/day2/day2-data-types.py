#Data Types
## Strings
"Jello"
#indexing with [] *note* indexing starts from 0!!
"Jello"[0]
# Getting the lengths of objects using the len function 
len("Jello")
# We can combine indexing and len to obtain the last character of a string
"Jello"[len("Jello")-1]
# alternatively, negative indexing would get us a similar result
"Jello"[-1]
"Jello"[-5]

#anything within quotes is a string! 
"123"+"345" # = "123345"

# Number Data Types
## Integer
123 + 345
#can use _ to make numbers more readable - computer ignores the underscores but we can visualize it more easily
123_345_345 * 2

## Float - floating point numbers
3.14159 

# Boolean
True 
False 

# to check the type of data, use the *type* function
num = 5
type(num)

# we can type cast - change the type of variable to another one, using str, int, float, etc.
str(num)

print("My chosen number is " + str(num))

## note: coercing to int removes all the numbers after the decimal. to have more accuracy/precision, use the 
## round function. you can also specify the amount of decimal places to round up to
round(5/3, 3)

#instead of dividing, you can use floor division, using //
8//3 # same as using int

# to perform self operations on a specific variable, we can use shorthand: +=, -=, *=, /= 
#sample
score = 1
score -=1 #adds 1 to the previous value of score and overwrites it

## F strings
# useful for combining strings with other data types 
score = 0 #integer
height = 1.8 #float
isWinning = True #boolean 

# in front of a string, we type f and replace variables with {}
print(f"your score is {score}, your height is {height}, you are winning is {isWinning}")
