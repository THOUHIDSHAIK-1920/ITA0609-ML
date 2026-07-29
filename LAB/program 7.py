"""
Logistic Regression example.
Loads the Iris dataset, trains a LogisticRegression model,
and prints accuracy and a small classification report.
"""
from __future__ import annotations

try:
    from sklearn.datasets import load_iris
    from sklearn.model_selection import train_test_split
    from sklearn.linear_model import LogisticRegression
    from sklearn.preprocessing import StandardScaler
    from sklearn.metrics import accuracy_score, classification_report
except Exception as exc:
    raise SystemExit(
        "This script requires scikit-learn. Install with: pip install scikit-learn"
    ) from exc


def main() -> None:
    data = load_iris()
    X = data.data
    y = data.target

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.3, random_state=42, stratify=y
    )

    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)

    model = LogisticRegression(max_iter=200)
    model.fit(X_train_scaled, y_train)

    y_pred = model.predict(X_test_scaled)

    acc = accuracy_score(y_test, y_pred)
    report = classification_report(y_test, y_pred, target_names=data.target_names)

    print(f"Accuracy: {acc:.4f}\n")
    print("Classification Report:")
    print(report)


if __name__ == "__main__":
    main()
