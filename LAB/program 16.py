"""program 16: Compare different classification algorithms and evaluate performance
Uses the Iris dataset and prints accuracy for several classifiers.
"""
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier
from sklearn.naive_bayes import GaussianNB


def main():
    data = load_iris()
    X_train, X_test, y_train, y_test = train_test_split(data.data, data.target, test_size=0.2, random_state=1)

    models = {
        'LogisticRegression': LogisticRegression(max_iter=200),
        'KNN': KNeighborsClassifier(),
        'SVC': SVC(),
        'RandomForest': RandomForestClassifier(n_estimators=100),
        'GaussianNB': GaussianNB()
    }

    for name, m in models.items():
        m.fit(X_train, y_train)
        preds = m.predict(X_test)
        print(f"{name} accuracy:", accuracy_score(y_test, preds))


if __name__ == '__main__':
    main()
