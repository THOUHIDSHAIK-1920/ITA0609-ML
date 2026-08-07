"""program 9: Compare Linear and Polynomial Regression
"""
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.pipeline import make_pipeline
from sklearn.datasets import make_regression
from sklearn.metrics import mean_squared_error


def main():
    X, y = make_regression(n_samples=100, n_features=1, noise=15.0, random_state=0)
    # add non-linearity
    X = np.sort(X, axis=0)
    y = y + 0.5 * X.ravel() ** 2

    lr = LinearRegression().fit(X, y)
    pr = make_pipeline(PolynomialFeatures(3), LinearRegression()).fit(X, y)

    lr_pred = lr.predict(X)
    pr_pred = pr.predict(X)

    print("Linear MSE:", mean_squared_error(y, lr_pred))
    print("Polynomial MSE:", mean_squared_error(y, pr_pred))

    try:
        plt.scatter(X, y, label='data')
        plt.plot(X, lr_pred, label='Linear', color='red')
        plt.plot(X, pr_pred, label='Poly deg3', color='green')
        plt.legend()
        plt.title('Linear vs Polynomial Regression')
        plt.show()
    except Exception:
        pass


if __name__ == '__main__':
    main()
