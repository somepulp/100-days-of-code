# Write a program to calculate the highest score from a list of scores
# similar inputs to exercise 1 - list of numbers
student_scores = input("Input a list of student scores ").replace(","," ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])

current_score = student_scores[0]
for score in student_scores:
    if score > current_score:
        current_score = score

print(f"The highest score in the class is: {current_score}")
