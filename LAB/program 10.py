from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
import numpy as np

def main():
    X = np.array([[20],[25],[30],[35],[40]])
    y = np.array([100,150,250,400,600])

    linear = LinearRegression()
    linear.fit(X, y)

    poly = PolynomialFeatures(degree=2)
    X_poly = poly.fit_transform(X)

    poly_model = LinearRegression()
    poly_model.fit(X_poly, y)

    try:
        temp = float(input("Enter Temperature: "))
    except Exception:
        print("Invalid input; using 30.0")
        temp = 30.0

    print("Linear Prediction:", linear.predict([[temp]])[0])
    print("Polynomial Prediction:", poly_model.predict(poly.transform([[temp]]))[0])


if __name__ == '__main__':
    main()
