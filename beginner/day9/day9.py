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



## NESTING
# List in a dictionary

capitals = {
     "France": "Paris",
     "Germany":"Berlin"
}

#travel log of cities you've been in each country:

travel_log = {
     "France":["Paris", "Lille", "Dijon"],
     "Germany": ["Berlin", "Hamburg", "Stuttgart"]
}

# Dictionary in a dictionary
travel_log = {
     "France":{
          "cities_visited":["Paris", "Lille", "Dijon"],
          "total_visits": [4,2,2]
     },
     "Germany": {
          "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
          "total_visits": 2
     }
}

# Dictionary in a list

travel_log = [
     {
          "country": "France",
          "cities_visited": ["Paris", "Lille", "Dijon"],
          "total_visits": [4,2,2]
     },
     {
          "country": "Germany",
          "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
          "total_visits": 2
     }
]

travel_log[0]['total_visits']
