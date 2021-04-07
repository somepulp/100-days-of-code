# Write a program that calculates the average student height from a list of heights
# avg height = sum of heights divided by total number of students
# round it to a whole number
# do not use the sum() or len() functions
# figure out how many items are in the list using a for loop, and add together using a for loop

# added replace to enable a comma separated list input
student_heights = input("Input a list of student heights ").replace(","," ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])

total_height = 0
num_students = 0
for height in student_heights:
    total_height += height
    num_students += 1

avg_height = round(total_height/num_students)
print(f"The average height for these students is: {avg_height}")