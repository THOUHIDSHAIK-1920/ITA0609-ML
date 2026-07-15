pin = int(input("Enter PIN: "))
amount = int(input("Enter amount: "))
balance = 10000
if pin == 1920:
    if amount <= balance:
        balance = balance - amount
        print("Withdrawal successful")
        print("Balance:", balance)
    else:
        print("Insufficient balance")
else:
    print("Wrong PIN")
