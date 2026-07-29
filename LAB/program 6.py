"""
Naive Bayes classifier example.
Loads the Iris dataset, trains a GaussianNB classifier,
and prints the confusion matrix and accuracy.
"""
from __future__ import annotations

try:
    from sklearn.datasets import load_iris
    from sklearn.model_selection import train_test_split
    from sklearn.naive_bayes import GaussianNB
    from sklearn.metrics import confusion_matrix, accuracy_score
    import numpy as np
    import pandas as pd
except Exception as exc:
    raise SystemExit(
        "This script requires scikit-learn, numpy and pandas. Install with: pip install scikit-learn numpy pandas"
    ) from exc


def main() -> None:
    data = load_iris()
    X = data.data
    y = data.target

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.3, random_state=42, stratify=y
    )

    model = GaussianNB()
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)

    cm = confusion_matrix(y_test, y_pred)
    acc = accuracy_score(y_test, y_pred)

    labels = data.target_names
    print("Confusion Matrix:")
    print(pd.DataFrame(cm, index=labels, columns=labels))
    print(f"\nAccuracy: {acc:.4f}")


if __name__ == "__main__":
    main()
