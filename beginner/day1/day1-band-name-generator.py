#Ask the user for the city they grew up in, and their pet's name. Then combined these variables to 
#produce their band name

# Create a greeting for the program
print("Welcome to the Band Name Generator.")
# Ask the user for the city they grew up in
city = input("What is the name of the city you grew up in?\n")
# Ask the user for the name of their pet
pet_name = input("What is your pet's name?\n")
# Combine both variables to show them their band name
msg = "Your band name could be "
print(msg + city + " " + pet_name)
