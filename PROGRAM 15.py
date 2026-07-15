temperatures = []
for i in range(7):
    temp = float(input("Enter temperature: "))
    temperatures.append(temp)
print("Maximum:", max(temperatures))
print("Minimum:", min(temperatures))
print("Average:", sum(temperatures) / 7)
