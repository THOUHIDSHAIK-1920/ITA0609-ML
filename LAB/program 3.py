from sklearn.tree import DecisionTreeClassifier

n = int(input("Enter number of samples: "))

X = []
Y = []

for i in range(n):
    print(f"\nSample {i+1}")
    age = int(input("Age: "))
    income = int(input("Income: "))
    buy = int(input("Buy (1=Yes,0=No): "))
    X.append([age, income])
    Y.append(buy)

model = DecisionTreeClassifier()
model.fit(X, Y)

print("\nEnter new sample")
age = int(input("Age: "))
income = int(input("Income: "))

result = model.predict([[age, income]])

if result[0] == 1:
    print("Prediction: Yes")
else:
    print("Prediction: No")
