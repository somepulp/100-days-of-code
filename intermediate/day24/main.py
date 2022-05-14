# Reading to a file
with open("my_file.txt") as file:
  contents = file.read()
  print(contents)


# Writing to a file 
with open("my_file.txt", mode="w") as file:
  file.write("Using mode = 'w' overwrites everything in the file with the new text")
