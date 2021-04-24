# Calculator Program

## Import packages and dependencies
from art import logo

# different functions of the calculator:

#Add
def add(n1, n2):
     return n1 + n2

#Subtract
def subtract(n1, n2):
     return n1 - n2

#Multiply
def multiply(n1, n2):
     return n1 * n2

#Divide
def divide(n1, n2):
     return n1 / n2


operations_dict = {
     "+": add,
     "-": subtract,
     "*": multiply,
     "/": divide,
}

num1 = int(input("What is the first number?: "))


# loop through dictionary and print out keys (for operations)
for key in operations_dict:
     print(key)

# ask user which operation they want to select
operand = input("Pick an operation from the line above: ")
num2 = int(input("What is the second number?: "))
op_function = operations_dict[operand]

answer = op_function(num1, num2)

print(f"{num1} {operand} {num2} = {answer}")