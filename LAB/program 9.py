from sklearn.linear_model import LinearRegression
import numpy as np


def main():
    X = np.array([[1], [2], [3], [4], [5]])
    y = np.array([2, 4, 6, 8, 10])
    model = LinearRegression()
    model.fit(X, y)
    try:
        n = float(input("Enter the value of X: "))
    except Exception:
        print("Invalid input; using X=6")
        n = 6.0
    prediction = model.predict([[n]])

    print("Predicted Y value is:", prediction[0])


if __name__ == '__main__':
    main()
