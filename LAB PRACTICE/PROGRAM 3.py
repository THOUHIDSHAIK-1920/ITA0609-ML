units = int(input("Enter units: "))
if units <= 100:
    bill = units * 1.5
elif units <= 200:
    bill = units * 2.5
else:
    bill = units * 4
print("Electricity Bill:", bill)
