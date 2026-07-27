salary = float(input("Enter basic salary: "))
pf = salary * 0.10
tax = salary * 0.05
gross = salary + 2000
net = gross - pf - tax
print("Gross Salary:", gross)
print("Net Salary:", net)
