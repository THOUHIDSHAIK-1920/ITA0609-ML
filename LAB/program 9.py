from sklearn.linear_model import LinearRegression
import numpy as np

X = np.array([[1],[2],[3],[4],[5],[6]])
y = np.array([35,45,55,65,75,85])

model = LinearRegression()
model.fit(X, y)

hours = float(input("Enter Study Hours: "))

print("Predicted Marks:", model.predict([[hours]])[0])


