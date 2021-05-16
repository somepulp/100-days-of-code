enemies = 1

def increase_enemies():
    #enemies += 2
    print(f"enemies inside function: {enemies}")
    return enemies + 1
increase_enemies()
print(f"enemies outside function: {enemies}")

weather = ["Sunny", "Cloudy", "Windy"]
def expand_weather():
     print(f"Last weather condition is: {weather[-1]}")
     return weather + ["Overcast"]
weather2 = expand_weather()
