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


operations = {
     "+": add,
     "-": subtract,
     "*": multiply,
     "/": divide,
}

num1 = int(input("What is the first number?: "))


# loop through dictionary and print out keys (for operations)
for key in operations:
     print(key)

# ask user which operation they want to select
operand = input("Pick an operation from the line above: ")
num2 = int(input("What is the second number?: "))
op_function = operations[operand]

answer = op_function(num1, num2)

print(f"{num1} {operand} {num2} = {answer}")

again = input("Type 'y' to continue calculating with {answer}, or type 'n' to exit: ")
continue_yes = True

while continue_yes:
     old_answer = answer
     operand = input("Pick an operation: ")
     num3 = int(input("What is the next number?: "))
     op_function = operations[operand]
     answer = op_function(old_answer, num3)
     print(f"{old_answer} {operand} {num3} = {answer}")
     again = input("Type 'y' to continue calculating with {answer}, or type 'n' to exit: ")
     if again == 'n':
          continue_yes = False