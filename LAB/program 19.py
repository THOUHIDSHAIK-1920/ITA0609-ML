"""program 19: Naive Bayes classification for Bank Loan prediction (synthetic)
"""
from sklearn.datasets import make_classification
from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, accuracy_score


def main():
    X, y = make_classification(n_samples=1000, n_features=12, n_informative=6, weights=[0.6, 0.4], random_state=10)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)
    clf = GaussianNB()
    clf.fit(X_train, y_train)
    preds = clf.predict(X_test)
    print("Accuracy:", accuracy_score(y_test, preds))
    print(classification_report(y_test, preds))


if __name__ == '__main__':
    main()
