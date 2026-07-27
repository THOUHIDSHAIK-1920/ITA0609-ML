hours = int(input("Enter parking hours: "))
if hours <= 2:
    fee = hours * 20
else:
    fee = hours * 30
print("Parking Fee:", fee)
