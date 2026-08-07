"""program 11: Credit Score Classification (synthetic example)
"""
import numpy as np
from sklearn.datasets import make_classification
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, accuracy_score


def main():
    X, y = make_classification(n_samples=1000, n_features=10, n_informative=6,
                               n_redundant=2, weights=[0.7, 0.3], random_state=42)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    clf = RandomForestClassifier(n_estimators=100, random_state=42)
    clf.fit(X_train, y_train)
    preds = clf.predict(X_test)
    print("Accuracy:", accuracy_score(y_test, preds))
    print(classification_report(y_test, preds))


if __name__ == '__main__':
    main()
