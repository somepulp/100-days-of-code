# Reading to a file
with open("my_file.txt") as file:
  contents = file.read()
  print(contents)


# Writing to a file 
with open("my_file.txt", mode="a") as file:
  file.write("\nUsing mode = 'a', the new text gets appended to the file, rather than replacing the old contents. Dont forget the newline character, if it's needed ('\\n') ")
