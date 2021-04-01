#Write a program that calculates the Body Mass Index (BMI) from a user's weight and height.
#bmi = kg/m^2

weight = float(input("Enter your weight in kgs:  "))
height = float(input("Enter your height in metres:  "))
bmi = weight/(height**2)
print("Your bmi is " + str(int(bmi)))