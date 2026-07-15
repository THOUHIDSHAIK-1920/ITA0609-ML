amount = float(input("Enter recharge amount: "))
if amount >= 500:
    cashback = 50
else:
    cashback = 0
final_amount = amount - cashback
print("Cashback:", cashback)
print("Final Amount:", final_amount)
