"""program 14: House Price Prediction using California housing dataset
"""
from sklearn.datasets import fetch_california_housing
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score


def main():
    data = fetch_california_housing()
    X_train, X_test, y_train, y_test = train_test_split(data.data, data.target, test_size=0.2, random_state=42)
    model = RandomForestRegressor(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    preds = model.predict(X_test)
    print("MSE:", mean_squared_error(y_test, preds))
    print("R2:", r2_score(y_test, preds))


if __name__ == '__main__':
    main()
