"""program 8: Linear Regression (simple example)
Uses sklearn's LinearRegression on synthetic data.
"""
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.datasets import make_regression
from sklearn.metrics import mean_squared_error, r2_score


def main():
    X, y = make_regression(n_samples=200, n_features=1, noise=20.0, random_state=42)
    model = LinearRegression()
    model.fit(X, y)
    preds = model.predict(X)
    print("Coefficients:", model.coef_)
    print("Intercept:", model.intercept_)
    print("MSE:", mean_squared_error(y, preds))
    print("R2:", r2_score(y, preds))


if __name__ == '__main__':
    main()
