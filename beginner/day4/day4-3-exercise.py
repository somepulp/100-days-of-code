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
#remove whitespace
position = position.replace(" ","")

#if they dont enter a 2 digit number, ask them to retry
if(len(position)<2):
    print("You have entered an invalid amount of coordinates!😣\nPlease ensure to select two digits which correspond to the column and row you would like to place the treasure on.")
else:
    col_num = int(position[0])
    row_num = int(position[1])
    if(col_num < 1 or col_num > len(row1) or row_num < 1 or row_num > len(map)):
        print("Invalid coordinates. Please select co-ordinates that exist on the map.\nNote: the first box is at coordinate (1,1)")
    else:
        map[row_num-1][col_num-1] = '❌'
        print(f"{map[0]}\n{map[1]}\n{map[2]}")