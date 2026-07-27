distance = float(input("Enter distance: "))
mileage = float(input("Enter mileage: "))
price = float(input("Enter fuel price: "))
fuel = distance / mileage
cost = fuel * price
print("Fuel needed:", fuel)
print("Total cost:", cost)
