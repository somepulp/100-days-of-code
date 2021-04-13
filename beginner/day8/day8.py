def greet():
    print("Hello")
    print("Nice day, huh?")
    print("Beautiful")

greet()

def greet_with_name(name):
    print(f"Hello, {name}")
    print("Nice day, huh?")

greet_with_name("Joy")

# Function with more than one input:
def greet_with(name, location):
    print(f"Hello, {name}")
    print(f"What's it like in {location}?")


greet_with("Joy", "Caledon")

greet_with(location="Caledon", name="Joy")