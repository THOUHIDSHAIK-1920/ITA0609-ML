seats = int(input("Enter number of seats: "))
price = float(input("Enter price per seat: "))
total = seats * price
if seats >= 5:
    discount = total * 0.10
else:
    discount = 0
final_cost = total - discount

print("Total Cost:", final_cost)
