# Calculate the sum of all the even numbers from 1 to 100 (inclusive)

total = 0
for number in range(0, 101, 2):
    total += number
print(total)