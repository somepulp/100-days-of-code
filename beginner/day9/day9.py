programming_dictionary = {
     "Bug": "An error in a program that prevents the program from running as expected.", 
     "Function": "A piece of code that you can easily call over and over again."
}

programming_dictionary["Loop"] = "The action of doing something repeatedly."
print(programming_dictionary)

empty_dictionary = {}

programming_dictionary["Bug"] = "A pain!"
print(programming_dictionary)

for thing in programming_dictionary:
     print(thing)
     print(programming_dictionary[thing])