# Write a program that interprets the BMI based on weight and height 

weight = float(input("What is your weight in kg? "))
height = float(input("What is your height in meters? "))

bmi = round(weight/(height**2),1)

if bmi < 18.5:
    print(f"bmi of {bmi} is considered underweight")
elif bmi < 25:
    print(f"bmi of {bmi} is considered normal")
elif bmi < 30:
    print(f"bmi of {bmi} is considered slightly overweight")
elif bmi < 35:
    print(f"bmi of {bmi} is considered obese")
else:
    print(f"bmi of {bmi} is considered clinically obese")