amount = float(input("Enter shopping amount: "))
if amount >= 2000:
    discount = amount * 0.10
else:
    discount = 0
bill = amount - discount
gst = bill * 0.05
total = bill + gst
print("Final Bill:", total)
