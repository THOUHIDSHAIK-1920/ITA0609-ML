"""program 20: Future Sales Prediction (time series) simple example
Uses sklearn regressor on lag features.
"""
import numpy as np
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error


def create_series(n=1000):
    np.random.seed(42)
    t = np.arange(n)
    series = 0.1 * t + 10 * np.sin(0.1 * t) + np.random.normal(scale=5.0, size=n)
    return series


def create_lag_features(series, lags=5):
    X, y = [], []
    for i in range(lags, len(series)):
        X.append(series[i - lags:i])
        y.append(series[i])
    return np.array(X), np.array(y)


def main():
    s = create_series(800)
    X, y = create_lag_features(s, lags=10)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    model = RandomForestRegressor(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    preds = model.predict(X_test)
    print("MSE:", mean_squared_error(y_test, preds))


if __name__ == '__main__':
    main()
