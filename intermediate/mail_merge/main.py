# Get list of invited names
with open("./input/names/invited_names.txt") as n:
    names = n.readlines()
names = [name.strip("\n") for name in names]

PLACEHOLDER = "[name]"

# Read letter template
with open("./input/letters/starting_letter.txt") as s:
    starting_letter = s.read()
    #Create and save a letter for each invited name 
    for name in names:
        new_letter = starting_letter.replace(PLACEHOLDER, name)
        with open(f"./output/readytosend/letter_for_{name}.txt", 'w') as l:
                l.write(new_letter)

