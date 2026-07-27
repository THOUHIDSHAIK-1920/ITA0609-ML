age = int(input("Enter age: "))
weight = float(input("Enter weight: "))
hemoglobin = float(input("Enter hemoglobin level: "))
if age >= 18 and weight >= 50 and hemoglobin >= 12.5:
    print("Eligible to donate blood")
else:
    print("Not eligible to donate blood")
