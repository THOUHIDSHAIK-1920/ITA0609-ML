"""program 9: Compare Linear and Polynomial Regression on the diabetes dataset.

This script uses the `bmi` feature from sklearn's diabetes dataset to
compare a linear regression model with a 3rd-degree polynomial regression.
"""
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_diabetes
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.pipeline import make_pipeline
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split


def main():
    X_full, y = load_diabetes(return_X_y=True)
    # use BMI feature (index 2) for a simple 1D comparison and visualization
    X = X_full[:, 2].reshape(-1, 1)

    # split so evaluation is on unseen data
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)

    lr = LinearRegression().fit(X_train, y_train)
    pr = make_pipeline(PolynomialFeatures(degree=3), LinearRegression()).fit(X_train, y_train)

    lr_pred = lr.predict(X_test)
    pr_pred = pr.predict(X_test)

    print("Linear MSE:", mean_squared_error(y_test, lr_pred))
    print("Polynomial (deg3) MSE:", mean_squared_error(y_test, pr_pred))

    # prepare curves for plotting (sorted by X)
    xs = np.linspace(X.min(), X.max(), 200).reshape(-1, 1)
    lr_curve = lr.predict(xs)
    pr_curve = pr.predict(xs)

    try:
        plt.scatter(X_test, y_test, label='test data', alpha=0.6)
        plt.plot(xs, lr_curve, label='Linear', color='red')
        plt.plot(xs, pr_curve, label='Poly deg3', color='green')
        plt.xlabel('BMI (feature)')
        plt.ylabel('Disease progression (target)')
        plt.legend()
        plt.title('Linear vs Polynomial Regression (diabetes: BMI feature)')
        plt.show()
    except Exception:
        # plotting may fail in headless environments; ignore silently
        pass


if __name__ == '__main__':
    main()
