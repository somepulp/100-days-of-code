# Get list of invited names
with open("./input/names/invited_names.txt") as n:
    names = n.readlines()
names = [name.strip("\n") for name in names]

# Get letter template
with open("./input/letters/starting_letter.txt") as file:
    starting_letter = file.readlines()
starting_letter = [line.strip("\n") for line in starting_letter]

#Create and save a letter for each invited name 
for name in names:
    new_letter = [line.replace("[name]", name) + "\n" for line in starting_letter]
    with open(f"./output/readytosend/letter_for_{name}.txt", 'w') as l:
            l.writelines(new_letter)
