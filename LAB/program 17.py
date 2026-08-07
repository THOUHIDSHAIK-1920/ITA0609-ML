"""program 17: Mobile Price Prediction (synthetic regression)
"""
from sklearn.datasets import make_regression
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score


def main():
    X, y = make_regression(n_samples=600, n_features=10, noise=25.0, random_state=7)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    model = GradientBoostingRegressor(n_estimators=200, random_state=42)
    model.fit(X_train, y_train)
    preds = model.predict(X_test)
    print("MSE:", mean_squared_error(y_test, preds))
    print("R2:", r2_score(y_test, preds))


if __name__ == '__main__':
    main()
