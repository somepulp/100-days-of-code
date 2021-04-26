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

def calculator():
     print(logo)

     num1 = float(input("What is the first number?: "))
     # loop through dictionary and print out keys (for operations)
     for key in operations:
          print(key)
     continue_yes = True

     while continue_yes:
          operand = input("Pick an operation: ")
          num2 = float(input("What is the next number?: "))
          op_function = operations[operand]
          answer = op_function(num1, num2)
          print(f"{num1} {operand} {num2} = {answer}")
          again = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ")
          if again == 'y':
               num1 = answer
          else:
               continue_yes = False
               calculator()

calculator()