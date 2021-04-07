# Write a program that marks a spot with an 'X'
# Using a two-digit system:
# - first digit = vertical column number
# - second digit = horizontal row number
# Program will take the user input (a two digit number), and print out marked spot

# starting code:
row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")

##Solution
#conversions to remove whitespace
first_digit = int(str(int(position))[0])
second_digit = int(str(int(position))[1])
if(first_digit < 1 or first_digit > len(row1) or second_digit<1 or second_digit>len(map)):
    print("Invalid coordinates. Please select co-ordinates that exist on the map.\nNote: the first box is at coordinate (1,1)")
else:
    map[second_digit-1][first_digit-1] = '❌'
    print(f"{map[0]}\n{map[1]}\n{map[2]}")