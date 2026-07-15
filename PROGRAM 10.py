age = int(input("Enter age: "))
fare = float(input("Enter ticket fare: "))
if age < 5:
    fare = 0
elif age >= 60:
    fare = fare / 2
print("Final Fare:", fare)
