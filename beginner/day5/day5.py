fruits = ["Apple", "Peach", "Pear"]

#print all items in the list one after another:
for fruit in fruits:
    print(fruit)
    print(fruit + " Pie")


# For loops using a range
for number in range(1, 10):
    print(number)

for number in range(11, 1, -2):
    print(number)

# Add up all numbers from 1 to 100:
total = 0
for number in range(1, 101):
    total += number
    print(total)