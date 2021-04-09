#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91

#to do: 
# - pick nrletters from letters list
letter_string = ""
for i in range(1, nr_letters+1):
    selected_letter = letters[random.randint(0, len(letters)-1)]
    letter_string += selected_letter

# - pick nrsymbols from symbols list, append to each other
symbol_string = ""
for s in range(1, nr_symbols+1):
    selected_symbol = symbols[random.randint(0, len(symbols)-1)]
    symbol_string += selected_symbol

# - pick nrnumbers from numbers list
number_string = ""
for s in range(1, nr_numbers+1):
    selected_number = numbers[random.randint(0, len(numbers)-1)]
    number_string += selected_number

final_password = letter_string + symbol_string + number_string
print("Here is your password: " + final_password)

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
#to randomize, can first get password string, and reshuffle characters
# or can try to randomize each position, based on the number of character of each item left..

# easier: shuffling characters
#final_pw_list = list(final_password)
password_length = len(final_password)
old_password = final_password
new_password = ""
for i in range(password_length):
    pl = len(final_password)
    random_index = random.randint(0, pl-1)
    selected_character = final_password[random_index]
    new_password += selected_character
    final_password = final_password.replace(selected_character, "",1)

print("Here is your password, randomized: " + new_password)