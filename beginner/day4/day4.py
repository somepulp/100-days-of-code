## Randomization

# import random

# random_integer = random.randint(1, 50)
# print(random_integer)

# #create a random floating point number between 0 and 1 
# print(random.random())

# #create a random floating point number between 0 and 5?
# random_float = random.random()
# print(random_float)
# #multiply by 5
# print(random_float*5)

## Lists
states_of_america = ["Delaware", "Pennsylvania", "New York"]
print(states_of_america[1])

states_of_america[1] = "Alaska"
print(states_of_america)

states_of_america.append("Arkansas")
print(states_of_america)

states_of_america.extend(["Minnesota", "California"])
print(states_of_america)