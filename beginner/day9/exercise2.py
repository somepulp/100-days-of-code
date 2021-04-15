# Write a program that writes to a travel log. 
# Create a function add_new_country that will add the entry for Russia to the travel_log: 
# add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])

travel_log = [
{
  "country": "France",
  "visits": 12,
  "cities": ["Paris", "Lille", "Dijon"]
},
{
  "country": "Germany",
  "visits": 5,
  "cities": ["Berlin", "Hamburg", "Stuttgart"]
},
]

def add_new_country(country, visits, cities_list):
     new_dict = {
          'country': country,
          'visits': visits,
          'cities': cities_list
     }
     travel_log.append(new_dict)

add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)