weight = float(input("Enter weight: "))
height = float(input("Enter height: "))
bmi = weight / (height * height)
print("BMI:", bmi)
if bmi < 18.5:
    print("Underweight")
elif bmi < 25:
    print("Normal")
elif bmi < 30:
    print("Overweight")
else:
    print("Obese")
