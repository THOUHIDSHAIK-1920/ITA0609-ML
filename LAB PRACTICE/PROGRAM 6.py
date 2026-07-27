food_bill = float(input("Enter food bill: "))
gst = food_bill * 0.05
service_charge = food_bill * 0.10
total = food_bill + gst + service_charge
print("Total Bill:", total)
